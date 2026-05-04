# Instagram Follow Diff

Analyze who doesn't follow you back on Instagram using HTML files.

✅ No API
✅ No login
✅ No scraping
✅ No external dependencies

---

## ⚡ Quick start

This repository already includes sample HTML files.

Just run:

```bash
python export_instagram_followers.py
```

---

## 🚀 Usage

Automatic mode (recommended):

```bash
python export_instagram_followers.py
```

Manual mode:

```bash
python export_instagram_followers.py followers.html following.html
```

---

## 📂 How it works

The script:

1. Looks for `.html` files in the same folder
2. Expects exactly **2 HTML files**
3. Automatically determines:

   * file with `i-follow` / `following` → **following**
   * the other file → **followers**

Then it compares both lists and finds users who don’t follow you back.

---

## 📥 Input files

This repository includes ready-to-use examples:

* `insa-fol-26.html`
* `insta-i-follow-26.html`

You can use them immediately or replace with your own files.

---

## 🛠 Using your own data

1. Open Instagram in browser

2. Go to:

   * Followers
   * Following

3. Scroll until **all users are loaded**

4. Open DevTools (Inspect)

5. Copy the list container:

   * Right-click → Copy → Copy outerHTML

6. Save as:

```
followers.html
following.html
```

Place files into the project folder.

---

## ⚠️ Important

* You MUST scroll fully before copying
* Partial scroll = incomplete results
* The script processes only the provided HTML

---

## 🧠 How it works internally

The script extracts usernames from links like:

```html
<a href="/username/">...</a>
```

It builds two sets:

* followers
* following

Then computes:

```
following - followers
```

---

## 📄 Output

Generated files:

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

## ⚖️ Legal Disclaimer

This project is not affiliated with, authorized, maintained, sponsored, or endorsed by Instagram or Meta.

This tool does not access Instagram directly.
It only processes HTML files provided by the user.

Users are responsible for ensuring their usage complies with applicable laws and platform terms.

---

## 🧩 Features

* Auto-detects HTML files
* Zero dependencies (pure Python)
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
├── insa-fol-26.html
├── insta-i-follow-26.html
└── README.md
```
