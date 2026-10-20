import os, wave, subprocess
import numpy as np
import cv2
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_IMG = os.path.join(ROOT, "public", "hero", "hero-portrait.webp")
AUDIO_PATH = os.path.join(ROOT, "public", "hero", "intro.wav")
FFMPEG = os.path.join(ROOT, "node_modules", "ffmpeg-static", "ffmpeg.exe")
OUT_DIR = os.path.join(ROOT, "public", "hero")
TEMP_VIDEO = os.path.join(ROOT, "public", "hero", "temp_raw.mp4")

# Load base image (768 x 960)
base_pil = Image.open(SRC_IMG).convert("RGB")
base_img = cv2.cvtColor(np.array(base_pil), cv2.COLOR_RGB2BGR)
H, W, _ = base_img.shape

# Load audio
wf = wave.open(AUDIO_PATH, "rb")
sr = wf.getframerate()
n_channels = wf.getnchannels()
n_frames = wf.getnframes()
raw_audio = wf.readframes(n_frames)
wf.close()

# Convert audio to mono float array
audio_data = np.frombuffer(raw_audio, dtype=np.int16).astype(np.float32) / 32768.0
if n_channels > 1:
    audio_data = audio_data.reshape(-1, n_channels).mean(axis=1)

duration = n_frames / sr
FPS = 24
total_video_frames = int(duration * FPS)
print(f"Audio duration: {duration:.2f}s, Total video frames: {total_video_frames} at {FPS} FPS")

# Precompute smoothed audio envelope for each video frame
samples_per_frame = sr / FPS
envelope = []
for i in range(total_video_frames):
    s_start = int(i * samples_per_frame)
    s_end = int(min(len(audio_data), (i + 1) * samples_per_frame))
    chunk = audio_data[s_start:s_end]
    if len(chunk) > 0:
        rms = np.sqrt(np.mean(chunk**2))
    else:
        rms = 0.0
    envelope.append(rms)

envelope = np.array(envelope)
# Smooth envelope with a 3-frame moving window
kernel = np.array([0.25, 0.5, 0.25])
smoothed_env = np.convolve(envelope, kernel, mode="same")
# Normalize
max_val = np.percentile(smoothed_env, 95)
if max_val > 0:
    smoothed_env = np.clip(smoothed_env / max_val, 0, 1.2)

# Face landmark anchor points in 768x960
# Mouth center at (384, 240)
MX, MY = 384, 240
MOUTH_W = 60
MOUTH_H = 14

# Eyes at (324, 180) and (444, 180)
LEX, LEY = 324, 180
REX, REY = 444, 180
EYE_R_X = 22
EYE_R_Y = 16

# Extract eye skin tone from forehead above eyes
skin_tone = base_img[140, 384].tolist() # BGR

# Create video writer
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
writer = cv2.VideoWriter(TEMP_VIDEO, fourcc, FPS, (W, H))

print("Rendering talking animation frames...")

for frame_idx in range(total_video_frames):
    t = frame_idx / FPS
    env = smoothed_env[frame_idx]

    frame = base_img.copy()

    # 1. Subtle breathing / body sway (1-2px)
    breath_dy = int(round(np.sin(t * 2.0 * np.pi / 2.8) * 1.5))
    head_nod = np.sin(t * 3.5) * (0.8 + env * 1.2) # subtle nod when speaking
    
    # 2. Eye Blinking (blink every ~3 seconds, lasting 5 frames)
    blink_cycle = t % 3.0
    blink_amount = 0.0
    if 2.7 <= blink_cycle <= 2.95:
        # Progress 0 -> 1 -> 0
        b_phase = (blink_cycle - 2.7) / 0.25
        blink_amount = np.sin(b_phase * np.pi)

    if blink_amount > 0.1:
        # Draw soft eyelid over left and right eyes
        for ex, ey in [(LEX, LEY), (REX, REY)]:
            lid_h = int(EYE_R_Y * blink_amount * 1.3)
            # Create an ellipse overlay
            cv2.ellipse(frame, (ex, ey - 2), (EYE_R_X, lid_h), 0, 0, 360, skin_tone, -1)
            # Subtle eyelid crease
            cv2.ellipse(frame, (ex, ey - 2), (EYE_R_X, lid_h), 0, 0, 180, (max(0, skin_tone[0]-35), max(0, skin_tone[1]-30), max(0, skin_tone[2]-25)), 1)

    # 3. Natural conversational head nod & breathing sway
    # No artificial 2D mouth cuts to avoid glitches. Natural face preserved cleanly.

    # 4. Subtle conversational head movement via slight affine tilt
    if abs(head_nod) > 0.3:
        M = cv2.getRotationMatrix2D((MX, MY), head_nod * 0.5, 1.0)
        # Apply to head area (y from 80 to 290)
        head_patch = frame[80:300, 260:510]
        M_patch = cv2.getRotationMatrix2D((MX - 260, MY - 80), head_nod * 0.4, 1.0)
        tilted_head = cv2.warpAffine(head_patch, M_patch, (510 - 260, 300 - 80), borderMode=cv2.BORDER_REFLECT)
        # Blend head patch
        mask = np.zeros((300 - 80, 510 - 260), dtype=np.float32)
        cv2.circle(mask, (MX - 260, MY - 80), 100, 1.0, -1)
        mask = cv2.GaussianBlur(mask, (21, 21), 0)[:, :, None]
        frame[80:300, 260:510] = (tilted_head * mask + frame[80:300, 260:510] * (1 - mask)).astype(np.uint8)

    writer.write(frame)

writer.release()
print("Raw video rendered to temp_raw.mp4")

# Multiplex with ffmpeg into hero.mp4 and hero.webm
out_mp4 = os.path.join(OUT_DIR, "hero.mp4")
out_webm = os.path.join(OUT_DIR, "hero.webm")

print("Encoding hero.mp4 with audio...")
cmd_mp4 = [
    FFMPEG, "-y",
    "-i", TEMP_VIDEO,
    "-i", AUDIO_PATH,
    "-c:v", "libx264", "-crf", "22", "-preset", "medium", "-pix_fmt", "yuv420p",
    "-c:a", "aac", "-b:a", "128k",
    "-movflags", "+faststart",
    "-shortest",
    out_mp4
]
subprocess.run(cmd_mp4, check=True)

print("Encoding hero.webm with audio...")
cmd_webm = [
    FFMPEG, "-y",
    "-i", TEMP_VIDEO,
    "-i", AUDIO_PATH,
    "-c:v", "libvpx-vp9", "-crf", "32", "-b:v", "0",
    "-c:a", "libopus", "-b:a", "96k",
    "-shortest",
    out_webm
]
subprocess.run(cmd_webm, check=True)

# Clean up temp raw video
if os.path.exists(TEMP_VIDEO):
    os.remove(TEMP_VIDEO)

print(f"SUCCESS: Generated {out_mp4} ({os.path.getsize(out_mp4):,} bytes) and {out_webm} ({os.path.getsize(out_webm):,} bytes)")
