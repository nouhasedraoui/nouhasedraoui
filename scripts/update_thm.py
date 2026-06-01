import requests, re

USERNAME = "rsd177"  # your THM username — no secret needed

def get_stats():
    # This is the confirmed-working public endpoint (no auth required)
    url = f"https://tryhackme.com/api/v2/public-profile/overview?username={USERNAME}"
    r = requests.get(url, timeout=10, headers={"User-Agent": "Mozilla/5.0"})
    r.raise_for_status()
    d = r.json()["data"]
    streak  = d.get("streak", {}).get("current", 0)
    rooms   = d.get("completedRooms", 0)
    rank    = d.get("globalPercentile", "N/A")
    return streak, rooms, rank

def update_readme(streak, rooms, rank):
    with open("README.md", "r", encoding="utf-8") as f:
        txt = f.read()

    txt = re.sub(r"Top \d+%",     f"Top {rank}%",       txt)
    txt = re.sub(r"\d+ Days 🔥",  f"{streak} Days 🔥",   txt)
    txt = re.sub(r"\d+ Rooms 🚪", f"{rooms} Rooms 🚪",   txt)

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(txt)

    print(f"✅ Streak: {streak} | Rank: Top {rank}% | Rooms: {rooms}")

streak, rooms, rank = get_stats()
update_readme(streak, rooms, rank)
