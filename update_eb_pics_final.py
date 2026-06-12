import re

mapping = {
    "Rachit": "Rachit.jpeg",
    "Darshini": "Darshini.jpeg"
}

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

for name, filename in mapping.items():
    pattern = r'<div class="eb-card-img-placeholder">.*?</div>(\s*<h4>' + re.escape(name) + r'</h4>)'
    replacement = r'<img src="./EB_PIcs/' + filename + r'" class="eb-card-img" alt="' + name + r'">\1'
    html = re.sub(pattern, replacement, html, count=1)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Updated final 2 EB pics")
