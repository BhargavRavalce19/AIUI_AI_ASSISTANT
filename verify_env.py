import os
from dotenv import load_dotenv

load_dotenv()

keys = ["WEATHER_API_KEY", "OPENAI_API_KEY", "NEWS_API_KEY", "TMDB_API_KEY", "EMAIL_USER", "EMAIL_PASS"]
missing = []
for key in keys:
    val = os.getenv(key)
    if not val:
        missing.append(key)
    else:
        # Print first few chars to verify (masking the rest)
        start = val[:4] if len(val) > 4 else "***"
        print(f"{key}: {start}...")

if missing:
    print(f"FAILED: Missing keys: {missing}")
    exit(1)
else:
    print("SUCCESS: All keys loaded correctly.")
