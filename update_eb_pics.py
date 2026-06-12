import re

mapping = {
    "Harshkumar Kedia": "Harshkumar.jpeg",
    "Kairav Shah": "Kairav.jpeg",
    "Dharmik Vasa": "Dharmik.jpeg",
    "Rishabhh Agarwaal": "Rishabh.jpeg",
    "Taher": "Taher.jpeg",
    "Uday": "Uday.jpeg",
    "Roshni": "Roshni.jpeg",
    "Udita": "Udita.jpeg",
    "Kunsh": "Kunsh.jpeg",
    "Vivaan": "Vivaan Shah.jpeg"
}

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

for name, filename in mapping.items():
    pattern = r'<div class="eb-card-img-placeholder">.*?</div>(\s*<h4>' + re.escape(name) + r'</h4>)'
    replacement = r'<img src="./EB_PIcs/' + filename + r'" class="eb-card-img" alt="' + name + r'">\1'
    html = re.sub(pattern, replacement, html, count=1)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

with open("style.css", "r", encoding="utf-8") as f:
    css = f.read()

if ".eb-card-img{" not in css:
    css = css.replace(".eb-card-img-placeholder{", ".eb-card-img{width:120px;height:140px;object-fit:cover;border-radius:var(--radius-sm);margin-bottom:12px;border:1px solid var(--gold-border)}\n.eb-card-img-placeholder{")
    with open("style.css", "w", encoding="utf-8") as f:
        f.write(css)

print("Updated EB pics")
