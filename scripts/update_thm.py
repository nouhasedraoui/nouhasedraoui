import requests, re, sys

USERNAME = "rsd177"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Accept": "application/json",
    "Referer": "https://tryhackme.com/"
}

def get_stats():
    # Try primary endpoint
    url = f"https://tryhackme.com/api/v2/public-profile/overview?username={USERNAME}"
    print(f"Trying: {url}")
    r = requests.get(url, timeout=15, headers=HEADERS)
    print(f"Status: {r.status_code}")
    print(f"Response: {r.text[:500]}")   # shows first 500 chars for debugging
    r.raise_for_status()
    d = r.json()["data"]
    streak = d.get("streak", {}).get("current", 0)
    rooms  = d.get("completedRooms", 0)
    rank   = d.get("globalPercentile", "N/A")
    return streak, rooms, rank

def update_readme(streak, rooms, rank):
    with open("README.md", "r", encoding="utf-8") as f:
        txt = f.read()
    txt = re.sub(r"Top \d+%",     f"Top {rank}%",      txt)
    txt = re.sub(r"\d+ Days 🔥",  f"{streak} Days 🔥",  txt)
    txt = re.sub(r"\d+ Rooms 🚪", f"{rooms} Rooms 🚪",  txt)
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(txt)
    print(f"✅ Updated → Streak: {streak} | Rank: Top {rank}% | Rooms: {rooms}")

try:
    streak, rooms, rank = get_stats()
    update_readme(streak, rooms, rank)
except Exception as e:
    print(f"❌ Error: {e}")
    sys.exit(1)
