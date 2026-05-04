"""
Instagram Unfollow Exporter
----------------------------
Zero external dependencies — works on Windows, macOS, Linux with any Python 3.6+.

Usage (optional — files are auto-detected if omitted):
    python export_instagram_followers.py [followers.html] [following.html]

How to get the HTML files:
    Instagram > Settings > Your activity > Download your information
    Open the downloaded ZIP, find the two HTML files for followers / following.
"""

import sys
import os
from html.parser import HTMLParser
from datetime import datetime


# ── HTML parser ──────────────────────────────────────────────────────────────

class _LinkParser(HTMLParser):
    """Collect Instagram profile links from the exported HTML."""

    def __init__(self):
        super().__init__()
        self.users = {}          # username -> display_name (insertion-ordered)
        self._pending = None     # username being captured

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            href = dict(attrs).get("href", "")
            # Instagram profile links look like  /username/
            if href.startswith("/") and href.count("/") == 2 and len(href) > 2:
                self._pending = href.strip("/")

    def handle_endtag(self, tag):
        if tag == "a":
            self._pending = None

    def handle_data(self, data):
        if self._pending and self._pending not in self.users:
            text = data.strip()
            if text:
                self.users[self._pending] = text


def extract_users(html_file):
    with open(html_file, "r", encoding="utf-8") as f:
        content = f.read()
    p = _LinkParser()
    p.feed(content)
    return p.users


# ── Plain-text writer ────────────────────────────────────────────────────────

def write_txt(path, title, users, ts):
    """Write *users* dict {username: display_name} to a human-readable .txt file.

    Adds the provided timestamp `ts` inside the file for traceability.
    """
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"{title}\n")
        f.write("=" * len(title) + "\n")
        f.write(f"Exported: {ts}\n")
        f.write(f"Total: {len(users)}\n\n")
        for i, (username, display_name) in enumerate(users.items(), start=1):
            name_part = f"{display_name}" if display_name else "(no display name)"
            f.write(f"{i:>4}.  {name_part}  (@{username})\n")


# ── Auto-detect HTML files ────────────────────────────────────────────────────

def _find_html_files():
    """
    Return (followers_path, following_path) by scanning HTML files in the
    script's directory.  Uses filename heuristics:
      - file whose name contains 'i-follow' / 'i_follow' / 'following' → "I follow"
      - remaining file → "my followers"
    Falls back to alphabetical order when exactly two files exist.
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    html_files = sorted(
        f for f in os.listdir(script_dir) if f.lower().endswith(".html")
    )
    if len(html_files) == 0:
        print("ERROR: No HTML files found in the script directory.")
        sys.exit(1)
    if len(html_files) == 1:
        print("ERROR: Only one HTML file found — need both followers and following.")
        sys.exit(1)
    if len(html_files) > 2:
        print("Found multiple HTML files:")
        for i, f in enumerate(html_files):
            print(f"  [{i}] {f}")
        print("Pass them explicitly:  python export_instagram_followers.py <followers> <following>")
        sys.exit(1)

    a, b = [os.path.join(script_dir, f) for f in html_files]
    following_keywords = ("i-follow", "i_follow", "following", "i follow")

    def _is_following(path):
        name = os.path.basename(path).lower()
        return any(kw in name for kw in following_keywords)

    if _is_following(b) and not _is_following(a):
        return a, b
    if _is_following(a) and not _is_following(b):
        return b, a
    # Cannot determine — treat alphabetically (first=followers, second=following)
    print(f"Note: auto-assigned  followers={html_files[0]}  following={html_files[1]}")
    return a, b


# ── Main ─────────────────────────────────────────────────────────────────────

if len(sys.argv) == 3:
    FOLLOWERS_FILE = sys.argv[1]
    FOLLOWING_FILE = sys.argv[2]
elif len(sys.argv) == 1:
    FOLLOWERS_FILE, FOLLOWING_FILE = _find_html_files()
else:
    print("Usage: python export_instagram_followers.py [followers.html] [following.html]")
    sys.exit(1)

print(f"Followers file : {FOLLOWERS_FILE}")
print(f"Following file : {FOLLOWING_FILE}")
print("Parsing...")

followers = extract_users(FOLLOWERS_FILE)
following = extract_users(FOLLOWING_FILE)

not_following_back = {u: following[u] for u in set(following) - set(followers)}

ts = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
out_dir = os.path.dirname(os.path.abspath(__file__))

followers_file  = os.path.join(out_dir, f"followers_{ts}.txt")
following_file  = os.path.join(out_dir, f"following_{ts}.txt")
not_back_file   = os.path.join(out_dir, f"not_following_back_{ts}.txt")

write_txt(followers_file,  "My Followers", followers, ts)
write_txt(following_file,  "Accounts I Follow", following, ts)
write_txt(not_back_file,   "I Follow — They Don't Follow Back", not_following_back, ts)

print("\nExported:")
print(f"  followers          -> {os.path.basename(followers_file)}  ({len(followers)} accounts)")
print(f"  following          -> {os.path.basename(following_file)}  ({len(following)} accounts)")
print(f"  not_following_back -> {os.path.basename(not_back_file)}  ({len(not_following_back)} accounts)")

