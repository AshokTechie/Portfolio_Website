import os
from PIL import Image, ImageDraw, ImageFont, ImageChops

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = r"C:\Users\thero\.gemini\antigravity\brain\b95e9fb8-c094-4e73-8175-6094061059c8\ashok_portrait_1792438392891.jpg"
OUT = os.path.join(ROOT, "public")
os.makedirs(os.path.join(OUT, "hero"), exist_ok=True)

paper = (244, 242, 238)
ink = (13, 13, 13)
mute = (119, 117, 111)

# Open source portrait
im = Image.open(SRC).convert("RGB")
w, h = im.size

# Target aspect ratio 4:5 (768 x 960)
# Centered crop
target_w = 800
target_h = int(target_w * 5 / 4) # 1000
crop_x = (w - target_w) // 2
crop_y = 10
cropped = im.crop((crop_x, crop_y, crop_x + target_w, crop_y + target_h))

# 1. portrait-bust.webp (480x600)
bust = cropped.resize((480, 600), Image.Resampling.LANCZOS)
bust.save(os.path.join(OUT, "portrait-bust.webp"), "WEBP", quality=92)
print("Saved portrait-bust.webp")

# 2. hero-portrait.webp (768x960)
hero_img = cropped.resize((768, 960), Image.Resampling.LANCZOS)
hero_img.save(os.path.join(OUT, "hero", "hero-portrait.webp"), "WEBP", quality=92)
hero_img.save(os.path.join(OUT, "hero", "hero-poster.webp"), "WEBP", quality=92)
print("Saved hero-portrait.webp and hero-poster.webp")

# 3. OG image (1200x630)
og = Image.new("RGB", (1200, 630), paper)
fig = cropped.resize((504, 630), Image.Resampling.LANCZOS)
bg = Image.new("RGB", (504, 630), paper)
og.paste(ImageChops.multiply(fig, bg), (696, 0))

d = ImageDraw.Draw(og)
def get_font(names, size):
    for name in names:
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            pass
    return ImageFont.load_default()

big = get_font(["arialbd.ttf", "calibrib.ttf", "DejaVuSans-Bold.ttf"], 118)
mid = get_font(["ariali.ttf", "georgiai.ttf", "DejaVuSerif-Italic.ttf"], 50)
sm = get_font(["arial.ttf", "calibri.ttf", "DejaVuSans.ttf"], 25)

d.text((72, 160), "Ashok H", font=big, fill=ink)
d.text((76, 310), "Software Engineer", font=mid, fill=mute)
d.text((76, 395), "Full-Stack & Cloud  |  ConnectSecure", font=sm, fill=ink)
og.save(os.path.join(OUT, "og.jpg"), "JPEG", quality=92)
print("Saved og.jpg")

# 4. Favicon & icon (AH mark)
S = 512
ic = Image.new("RGBA", (S, S), (0, 0, 0, 0))
draw = ImageDraw.Draw(ic)
draw.ellipse((0, 0, S - 1, S - 1), fill=ink + (255,))
f = get_font(["arialbd.ttf", "calibrib.ttf", "DejaVuSans-Bold.ttf"], 210)
bb = draw.textbbox((0, 0), "AH", font=f)
tx = (S - (bb[2] - bb[0])) / 2 - bb[0]
ty = (S - (bb[3] - bb[1])) / 2 - bb[1]
draw.text((tx, ty), "AH", font=f, fill=paper)
ic.save(os.path.join(OUT, "icon.png"))
ic.save(os.path.join(OUT, "favicon.ico"), sizes=[(16, 16), (32, 32), (48, 48)])
print("Saved icon.png and favicon.ico")
print("All assets successfully generated!")
