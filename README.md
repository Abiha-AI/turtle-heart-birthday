<div align="center">

# 💖 Happy Birthday Heart
### A Python Turtle Graphics Love Letter

*A tiny, sweet script that draws a mathematical heart — stitched together entirely out of a name, written over and over along the curve.*

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Turtle Graphics](https://img.shields.io/badge/Turtle-Graphics-FF69B4?style=for-the-badge)
![Made with Love](https://img.shields.io/badge/Made%20with-💗-red?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-2ECC71?style=for-the-badge)

</div>

---

## ✨ Preview

<div align="center">

*(Add your screenshot here — see the "Adding a Preview Image" section below)*

![Heart Preview](preview.png)

</div>

The script opens a **pink canvas** and traces a heart outline using the classic *heart curve formula*, stamping a name at each point along the path — creating a "written entirely in text" heart effect. 🌸

---

## 🚀 Getting Started

### 📦 Prerequisites

- Python 3.x — `turtle` ships with the standard library, so **no extra installs needed**.

> 🐧 **Linux users:** you may need Tkinter separately:
> ```bash
> sudo apt-get install python3-tk
> ```

### ▶️ Running the Script

```bash
# 1. Clone this repository
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

# 2. Run it
python heart.py
```

A pink window will pop up and draw the heart automatically. 💗

---

## 🛠️ Customization Guide

| 🎨 What you want to change | 📍 Where to edit |
|---|---|
| Name displayed on the heart | Replace `"Your Name"` in `pen.write(...)` |
| Background color | Change `window.bgcolor("Pink")` → any [Tkinter color](https://www.tcl.tk/man/tcl8.6/TkCmd/colors.htm) or hex code |
| Heart/text color | Change `pen.color("#864104")` |
| Font style | Edit `font=("Times New Roman", 7, "bold")` |
| Heart size | Adjust the `* 12` scale factor on `x` and `y` |
| Curve smoothness | Increase/decrease the `points` variable |
| Drawing speed | Change `pen.speed(0)` (0 = instant, 1–10 = slower) |

---

## 🧮 How It Works

The heart shape is generated using a well-known **parametric heart equation**:

```
x(t) = 16 sin³(t)
y(t) = 13 cos(t) − 5 cos(2t) − 2 cos(3t) − cos(4t)
```

The script loops `t` from `0` to `2π` in small increments, computes `(x, y)` for each step, moves the pen there without drawing a line (`penup()`), and **writes the given name as text** at that coordinate — so the outline of the heart is formed entirely out of repeated name-stamps rather than a solid line. ✨

---

## 📄 File Structure

```
📁 turtle-heart-birthday
├── 🐍 heart.py       # Main script
├── 🖼️ preview.png     # Screenshot of the drawing (add your own)
└── 📘 README.md       # This file
```

---

## 📋 Requirements

| Package | Type |
|---|---|
| `turtle` | Standard library ✅ |
| `math` | Standard library ✅ |

No `pip install` required — everything used here ships with Python. 🎉

---

## 🤝 Contributing

Feel free to fork this repo and customize it for your own occasions — birthdays, anniversaries, Valentine's Day, or just for fun. Pull requests for new shapes, animations, or color themes are always welcome! 🌟

## 📜 License

This project is open source and available under the [MIT License](LICENSE).

<div align="center">

---

Made with 🐍 + 💗 using Python Turtle Graphics

</div>
