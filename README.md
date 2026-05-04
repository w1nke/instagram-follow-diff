# Instagram Follow Diff

Analyze who doesn't follow you back on Instagram using HTML copied directly from the web interface.

✅ No API
✅ No login
✅ No scraping
✅ No external dependencies

---

## 🚀 Usage

```bash
python export_instagram_followers.py
```

Or manually:

```bash
python export_instagram_followers.py followers.html following.html
```

---

## 📥 How to get data (required)

This tool works with HTML copied from Instagram in your browser.

### Step-by-step

1. Open Instagram in your browser

2. Go to your:

   * **Followers**
   * **Following**

3. Scroll all the way down until **all users are loaded**
   (Instagram loads users dynamically)

4. Right-click → **Inspect (DevTools)**

5. Find the container with the users list

6. Right-click → **Copy → Copy outerHTML**

7. Save into files:

```
followers.html
following.html
```

---

## ⚠️ Important

* You MUST scroll fully before copying
* Partial scroll = incomplete results
* The script only processes what exists in the HTML

---

## 🧠 How it works

The script parses HTML and extracts profile links like:

```html
<a href="/username/">...</a>
```

Usernames are extracted from these links and compared between lists.

---

## 📄 Output

The script generates:

* `followers_YYYY-MM-DD_HH-MM-SS.txt`
* `following_YYYY-MM-DD_HH-MM-SS.txt`
* `not_following_back_YYYY-MM-DD_HH-MM-SS.txt`

Example:

```
I Follow — They Don't Follow Back
================================
Exported: 2026-05-04_10-30-22
Total: 3

1. user1 (@user1)
2. user2 (@user2)
3. user3 (@user3)
```

---

## 📂 Example input

This repository includes sample files:

* `insa-fol-26.html`
* `insta-i-follow-26.html`

---

## ⚖️ Legal Disclaimer

This project is not affiliated with, authorized, maintained, sponsored, or endorsed by Instagram or Meta.

This tool does not access Instagram directly.
It only processes HTML provided by the user.

Users are responsible for ensuring their usage complies with applicable laws and platform terms.

---

## 🧩 Features

* Auto-detects HTML files in directory
* No dependencies (pure Python)
* Works offline
* Simple and fast

---

## 🧑‍💻 Notes

* HTML structure may change if Instagram updates UI
* Designed for personal use

---

## 📌 Project structure

```
.
├── export_instagram_followers.py
├── followers.html
├── following.html
└── README.md
```
