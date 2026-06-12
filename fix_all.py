import os
import re

# 1. Update style.css
with open("style.css", "r", encoding="utf-8") as f:
    css = f.read()

# Replace gold variables
css = css.replace("--gold:#fdc934;", "--gold:#ccb17c;")
css = css.replace("--gold-light:#ffe07a;", "--gold-light:#e5d1a4;")
css = css.replace("--gold-dark:#cc9c1a;", "--gold-dark:#a98743;")
css = css.replace("--gold-border:rgba(253,201,52,0.25);", "--gold-border:rgba(204,177,124,0.25);")
css = css.replace("--gold-glow:0 0 20px rgba(253,201,52,0.12);", "--gold-glow:0 0 20px rgba(204,177,124,0.12);")

# Update placeholder sizes if needed
css = css.replace("width:160px;height:180px;", "width:120px;height:140px;")
css = css.replace("font-size:3rem;margin-bottom:16px", "font-size:2rem;margin-bottom:12px")

# Also the .eb-title-img size might be too big
css = css.replace(".eb-title-img{width:32px;height:32px;object-fit:contain}", ".eb-title-img{width:20px;height:20px;object-fit:contain;margin-right:8px;}")

with open("style.css", "w", encoding="utf-8") as f:
    f.write(css)

# 2. Update index.html to revert broken SVGs to FontAwesome
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

broken = {
    "GDWC": "fa-jet-fighter",
    "UNODC": "fa-handcuffs",
    "UNHRC": "fa-hands-holding-child",
    "IAEA": "fa-radiation"
}

for c, fa in broken.items():
    # In committee headers and EB titles
    html = html.replace(f'<img src="./ICONS/{c}.svg" class="committee-img">', f'<i class="fa-solid {fa}"></i>')
    html = html.replace(f'<img src="./ICONS/{c}.svg" class="eb-title-img">', f'<i class="fa-solid {fa}"></i>')
    # In onclick handler
    html = html.replace(f"<img src=\\'./ICONS/{c}.svg\\' class=\\'committee-img\\'>", f"<i class=\\'fa-solid {fa}\\'></i>")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

# 3. Recolor valid SVGs to new gold (#ccb17c)
for name in ["UNSC", "AIPPM"]:
    path = f"ICONS/{name}.svg"
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            data = f.read()
        data = data.replace("#fdc934", "#ccb17c")
        with open(path, "w", encoding="utf-8") as f:
            f.write(data)

print("Fixed CSS, HTML, and SVGs")
