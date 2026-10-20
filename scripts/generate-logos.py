import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOGOS_DIR = os.path.join(ROOT, "public", "logos")

LOGOS = {
    "nodejs.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 289">
  <path fill="#339933" d="M128 0L0 74v148l128 74 128-74V74L128 0zm0 25L234 86v124l-106 61-106-61V86L128 25z"/>
  <path fill="#339933" d="M128 42l88 51v102l-88 51-88-51V93l88-51z"/>
  <path fill="#ffffff" d="M128 65l68 39v78l-68 39-68-39v-78l68-39z"/>
</svg>''',

    "express.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256">
  <rect width="256" height="256" rx="40" fill="#000000"/>
  <text x="50%" y="54%" font-family="system-ui, -apple-system, sans-serif" font-size="44" font-weight="900" fill="#ffffff" text-anchor="middle" dominant-baseline="middle" letter-spacing="-1">express</text>
  <path d="M50 170 h156" stroke="#ffffff" stroke-width="6" stroke-linecap="round"/>
</svg>''',

    "tailwindcss.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 154">
  <path fill="#38BDF8" d="M128 0C93.9 0 72.5 17.1 64 51.3c12.8-17.1 27.7-23.5 44.8-19.2 9.8 2.5 16.7 9.6 24.5 17.5C146 62.6 161.4 78 192 78c34.1 0 55.5-17.1 64-51.3-12.8 17.1-27.7 23.5-44.8 19.2-9.8-2.5-16.7-9.6-24.5-17.5C174 15.4 158.6 0 128 0zM64 76C29.9 76 8.5 93.1 0 127.3c12.8-17.1 27.7-23.5 44.8-19.2 9.8 2.5 16.7 9.6 24.5 17.5 12.7 13 28.1 28.4 58.7 28.4 34.1 0 55.5-17.1 64-51.3-12.8 17.1-27.7 23.5-44.8 19.2-9.8-2.5-16.7-9.6-24.5-17.5C110 91.4 94.6 76 64 76z"/>
</svg>''',

    "fastapi.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256">
  <circle cx="128" cy="128" r="128" fill="#009688"/>
  <path fill="#ffffff" d="M139.6 34.1L57.9 144.9h54.9l-14.4 77 81.7-110.8h-54.9l14.4-77z"/>
</svg>''',

    "gcp.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 206">
  <path fill="#EA4335" d="M194.2 81.6c-4.4-30.8-31-54.6-63.2-54.6-25.2 0-47.1 14.5-57.8 35.5-6.3-4.2-13.9-6.7-22.2-6.7-21.5 0-39 17.5-39 39 0 3.2.4 6.3 1.1 9.3C5.6 109.8 0 119.2 0 130c0 19.3 15.7 35 35 35h155c27.6 0 50-22.4 50-50 0-24.8-18.1-45.4-41.8-49.4"/>
  <path fill="#4285F4" d="M190 165H35c-19.3 0-35-15.7-35-35 0-10.8 5.6-20.2 13.1-25.9 7.4-5.6 16.7-9.1 26.9-9.1 3.5 0 6.9.4 10.1 1.2 10.7-21 32.6-35.5 57.8-35.5 17.5 0 33.4 7 45 18.3 11.6 11.3 18.8 27 18.8 44.3 0 3.2-.3 6.3-.9 9.3 22.8 3.8 40.2 23.6 40.2 47.4 0 27.6-22.4 50-50 50z"/>
  <path fill="#FBBC05" d="M130.8 60.7c-25.2 0-47.1 14.5-57.8 35.5 10.7 7.7 23.8 12.3 38 12.3 25.2 0 46.8-14.7 57.5-35.8-10.8-7.5-23.7-12-37.7-12z"/>
  <path fill="#34A853" d="M190 165h-79c23.2 0 43.1-13.3 53-32.8 14.4 3.7 25 16.9 26 32.8z"/>
</svg>''',

    "firebase.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 352">
  <path fill="#FFA000" d="M0 282.8l1.4-2.8L106.8 84.4l.6-3.8c.8-5.2 5.6-8.8 10.8-7.9 3.2.5 5.9 2.5 7.3 5.4l28.7 57.1L0 282.8z"/>
  <path fill="#F57C00" d="M153.2 4.4c-4.4-3.1-10.3-2.6-14.1 1.2L0 282.8l128 72 128-72L153.2 4.4z"/>
  <path fill="#FFCA28" d="M256 282.8L154.2 89.2c-3.1-5.9-10.5-8.2-16.4-5.1-2.9 1.5-5 4.1-5.8 7.2L0 282.8l128 72 128-72z"/>
</svg>''',

    "git.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256">
  <path fill="#F05032" d="M251.2 115.8L140.2 4.8c-6.4-6.4-16.8-6.4-23.2 0L93.7 28.2l34.8 34.8c7.6-2.6 16.3-.9 22.4 5.2 6.1 6.1 7.8 14.8 5.2 22.4l33.5 33.5c7.6-2.6 16.3-.9 22.4 5.2 8.7 8.7 8.7 22.7 0 31.4-8.7 8.7-22.7 8.7-31.4 0-6.4-6.4-8-15.7-4.7-23.6l-31.3-31.3v58.2c2.4 1.2 4.7 2.8 6.6 4.7 8.7 8.7 8.7 22.7 0 31.4-8.7 8.7-22.7 8.7-31.4 0-8.7-8.7-8.7-22.7 0-31.4 2.3-2.3 5.1-4 8.1-5.1V89.4c-3-1.1-5.8-2.8-8.1-5.1-6.4-6.4-8-15.7-4.7-23.6L79.8 25.8 4.8 100.8c-6.4 6.4-6.4 16.8 0 23.2l111 111c6.4 6.4 16.8 6.4 23.2 0l112.2-112.2c6.4-6.4 6.4-16.8 0-23.2z"/>
</svg>''',

    "postman.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256">
  <circle cx="128" cy="128" r="128" fill="#FF6C37"/>
  <path fill="#ffffff" d="M192.5 116.8c-2.4-.7-4.9-1.2-7.5-1.4l11.4-15.6c1.6-2.2 1.1-5.3-1.1-6.9-2.2-1.6-5.3-1.1-6.9 1.1l-13.8 18.9c-11.8-3.1-24.4-4-37-2.6-1.6.2-3.1.4-4.7.7l-9.8-19.6c-1.2-2.4-4.2-3.4-6.6-2.2-2.4 1.2-3.4 4.2-2.2 6.6l9.3 18.6c-19.8 6.1-37.4 18-50.6 34.2-1.8 2.2-1.5 5.4.7 7.2 2.2 1.8 5.4 1.5 7.2-.7 12-14.7 28-25.5 46-31l-18.7 41.2c-1.1 2.5 0 5.4 2.5 6.5 2.5 1.1 5.4 0 6.5-2.5l20.4-44.9c10.3-.9 20.6-.2 30.6 2.2l-37 50.8c-1.6 2.2-1.1 5.3 1.1 6.9 2.2 1.6 5.3 1.1 6.9-1.1l38.2-52.4c10.1 3.5 19.3 9.2 27.2 16.6 2 1.9 5.2 1.8 7.1-.2 1.9-2 1.8-5.2-.2-7.1-8.5-8-18.6-14.2-29.6-18.3z"/>
</svg>''',

    "cpp.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 288">
  <path fill="#00599C" d="M128 0L0 74v140l128 74 128-74V74L128 0zm108 202.4L128 264.8 20 202.4V85.6L128 23.2l108 62.4v116.8z"/>
  <path fill="#004482" d="M128 23.2v241.6l108-62.4V85.6L128 23.2z"/>
  <text x="44%" y="54%" font-family="system-ui, -apple-system, sans-serif" font-size="76" font-weight="900" fill="#ffffff" text-anchor="middle" dominant-baseline="middle">C++</text>
</svg>''',

    "c.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 288">
  <path fill="#A8B9CC" d="M128 0L0 74v140l128 74 128-74V74L128 0zm108 202.4L128 264.8 20 202.4V85.6L128 23.2l108 62.4v116.8z"/>
  <path fill="#5C6F84" d="M128 23.2v241.6l108-62.4V85.6L128 23.2z"/>
  <text x="50%" y="54%" font-family="system-ui, -apple-system, sans-serif" font-size="90" font-weight="900" fill="#ffffff" text-anchor="middle" dominant-baseline="middle">C</text>
</svg>''',

    "java.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 348">
  <path fill="#EA2D2E" d="M96.7 268.4s-14.7 9.2 10.3 12.3c30.2 3.8 45.6 3.5 78.4-4.1 0 0 11 7 24.3 13-41.9 16.9-97.7 13.9-129.5-3.6-13.8-7.7-8.3-15.6 16.5-17.6zm-5.7-44.4s-16.7 12 8.7 15.3c35.2 4.6 62.8 5 110.1-6.1 0 0 7.7 5.7 17.5 10.5-54.6 18.7-124.7 15-155.8-3.7-17-10.3-6.9-14.4 19.5-16zm63.4-60.6c13.7 15.8-3.6 30.1-3.6 30.1s35-18.1 18.7-41.1c-15.4-21.7-29.3-32.6 39.3-69.6 0 0-93.5 24.7-54.4 80.6z"/>
  <path fill="#5382A1" d="M228.6 288.7c-54.6 18.7-124.7 15-155.8-3.7-5.9-3.6-9.2-7.2-10.4-10.8 14.1 4.5 32.7 7.7 55.6 8.7 44.9 2 81.3-4.5 110.6-12.7v18.5zm-14.7-184.2c-15.4-21.7-29.3-32.6 39.3-69.6 0 0-93.5 24.7-54.4 80.6 13.7 15.8-3.6 30.1-3.6 30.1s35-18.1 18.7-41.1z"/>
</svg>''',

    "langchain.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256">
  <rect width="256" height="256" rx="52" fill="#0E2B3D"/>
  <path d="M70 128c0-22 18-40 40-40h36c22 0 40 18 40 40s-18 40-40 40h-36c-22 0-40-18-40-40z" fill="none" stroke="#1C3C3C" stroke-width="24"/>
  <path d="M80 128h96" stroke="#2DE0A5" stroke-width="20" stroke-linecap="round"/>
  <circle cx="80" cy="128" r="24" fill="#2DE0A5"/>
  <circle cx="176" cy="128" r="24" fill="#2DE0A5"/>
  <circle cx="128" cy="80" r="16" fill="#F4B400"/>
  <circle cx="128" cy="176" r="16" fill="#F4B400"/>
</svg>''',

    "langgraph.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256">
  <rect width="256" height="256" rx="52" fill="#1A1A2E"/>
  <path d="M70 70 L186 70 L128 186 Z" fill="none" stroke="#E94560" stroke-width="14" stroke-linejoin="round"/>
  <circle cx="70" cy="70" r="24" fill="#0F3460" stroke="#E94560" stroke-width="8"/>
  <circle cx="186" cy="70" r="24" fill="#0F3460" stroke="#E94560" stroke-width="8"/>
  <circle cx="128" cy="186" r="26" fill="#E94560"/>
  <circle cx="128" cy="186" r="12" fill="#ffffff"/>
</svg>''',

    "qdrant.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256">
  <rect width="256" height="256" rx="52" fill="#DC2626"/>
  <polygon points="128,40 216,90 216,166 128,216 40,166 40,90" fill="#B91C1C"/>
  <polygon points="128,40 216,90 128,140 40,90" fill="#EF4444"/>
  <polygon points="128,140 216,90 216,166 128,216" fill="#991B1B"/>
  <circle cx="128" cy="128" r="28" fill="#ffffff"/>
</svg>''',

    "gemini.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256">
  <defs>
    <linearGradient id="geminiGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1BA1E3"/>
      <stop offset="50%" stop-color="#5B6CF9"/>
      <stop offset="100%" stop-color="#9C40FF"/>
    </linearGradient>
  </defs>
  <rect width="256" height="256" rx="52" fill="#0F1117"/>
  <path d="M128 20 C128 79.6 176.4 128 236 128 C176.4 128 128 176.4 128 236 C128 176.4 79.6 128 20 128 C79.6 128 128 79.6 128 20 Z" fill="url(#geminiGrad)"/>
</svg>''',

    "connectsecure.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256">
  <rect width="256" height="256" rx="52" fill="#0B132B"/>
  <path d="M128 40 L200 75 V135 C200 180 168 215 128 226 C88 215 56 180 56 135 V75 Z" fill="#1C2541" stroke="#48CAE4" stroke-width="12" stroke-linejoin="round"/>
  <path d="M100 130 L120 150 L160 106" fill="none" stroke="#48CAE4" stroke-width="16" stroke-linecap="round" stroke-linejoin="round"/>
</svg>''',

    "uvce.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256">
  <rect width="256" height="256" rx="52" fill="#1A365D"/>
  <circle cx="128" cy="128" r="88" fill="none" stroke="#ECC94B" stroke-width="8"/>
  <text x="50%" y="46%" font-family="Georgia, serif" font-size="34" font-weight="900" fill="#ECC94B" text-anchor="middle" dominant-baseline="middle">UVCE</text>
  <text x="50%" y="68%" font-family="system-ui, sans-serif" font-size="16" font-weight="700" fill="#ffffff" text-anchor="middle" dominant-baseline="middle" letter-spacing="2">ESTD 1917</text>
</svg>''',
}

for filename, content in LOGOS.items():
    path = os.path.join(LOGOS_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Wrote {filename}")

print("All brand SVGs successfully generated!")
