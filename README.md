# Instagram Follow Diff

Find who doesn’t follow you back on Instagram using HTML files.

✅ No API
✅ No login
✅ No scraping
✅ No dependencies

---

## 🧰 Setup (first time only)

### 1. Install Python

* Download: https://www.python.org/downloads/
* During installation (Windows): ✔ **Add Python to PATH**

Verify:

```bash
python --version
```

---

### 2. Install VS Code (optional but recommended)

* Download: https://code.visualstudio.com/
* Open the project folder in VS Code

---

### 3. Download this project

* Click **Code → Download ZIP**
* Unzip the folder

---

## ⚡ Quick start

Sample HTML files are already included.

Just run:

```bash
python export_instagram_followers.py
```

---

## 📥 How to get your data

1. Open Instagram in browser

2. Go to:

   * Followers
   * Following

3. Scroll to the very bottom (Instagram loads users dynamically)

4. Open DevTools (**Inspect**)

5. Find and copy the main list container:

```html
<div style="display: flex; flex-direction: column; padding-bottom: 0px; padding-top: 0px; position: relative;">
```

👉 Copy the entire block (**Copy outerHTML**)

---

## 📂 Insert into project

1. Open:

* `insa-fol-26.html` → paste Followers
* `insta-i-follow-26.html` → paste Following

2. Replace existing content with your copied HTML

---

## ▶️ Run

In VS Code:

👉 Click **Run**
or use terminal:

```bash
python export_instagram_followers.py
```

---

## 📄 Output

The script generates:

* followers_*.txt
* following_*.txt
* not_following_back_*.txt

---

## 🧠 How it works

* Reads HTML files from the project folder
* Extracts usernames from:

```html
<a href="/username/">
```

* Compares:

```
following - followers
```

---

## ⚠️ Important

* You MUST scroll fully before copying
* Partial data = wrong results
* Script works only with provided HTML

---

## ⚖️ Legal

Not affiliated with Instagram / Meta.
No direct access — only processes user-provided HTML.

---

## 📌 Structure

```
.
├── export_instagram_followers.py
├── insa-fol-26.html
├── insta-i-follow-26.html
└── README.md
```
