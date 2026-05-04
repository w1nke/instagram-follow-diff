import sys
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

def extract_users(html_file):
    with open(html_file, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")

    users = {}
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if href.startswith("/") and href.count("/") == 2:
            username = href.strip("/")
            display_name = a.get_text(strip=True)
            users[username] = display_name

    return users

if len(sys.argv) < 3:
    print("Usage: python3 export_instagram_followers.py followers.html following.html")
    sys.exit(1)

FOLLOWERS_FILE = sys.argv[1]
FOLLOWING_FILE = sys.argv[2]

followers = extract_users(FOLLOWERS_FILE)
following = extract_users(FOLLOWING_FILE)

# Convert to DataFrames
df_followers = pd.DataFrame(
    [{"username": u, "display_name": n} for u, n in followers.items()]
)

df_following = pd.DataFrame(
    [{"username": u, "display_name": n} for u, n in following.items()]
)

# People you follow who don't follow you back
not_following_back = set(following.keys()) - set(followers.keys())

df_not_back = pd.DataFrame(
    [{"username": u, "display_name": following.get(u, "")} for u in not_following_back]
)

# Timestamp
ts = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# Filenames with timestamp
followers_file = f"followers_{ts}.xlsx"
following_file = f"following_{ts}.xlsx"
not_back_file = f"not_following_back_{ts}.xlsx"

# Save files
df_followers.to_excel(followers_file, index=False)
df_following.to_excel(following_file, index=False)
df_not_back.to_excel(not_back_file, index=False)

print("✅ Exported:")
print(f"   - {followers_file} ({len(df_followers)})")
print(f"   - {following_file} ({len(df_following)})")
print(f"   - {not_back_file} ({len(df_not_back)})")
