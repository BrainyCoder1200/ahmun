import re

# 1. Update index.html
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

new_btn = """                <div class="modal-section" style="margin-top: 30px; text-align: center;">
                    <a id="meet-eb-btn" href="#" class="btn btn-gold btn-full" onclick="closeCommitteeModal()">Meet the EB</a>
                </div>
            </div>"""

if 'id="meet-eb-btn"' not in html:
    html = html.replace('            </div>\n        </div>\n    </div>', new_btn + '\n        </div>\n    </div>')

html = html.replace('<!-- UNSC -->\n                    <div class="eb-group animate-trigger">', '<!-- UNSC -->\n                    <div class="eb-group animate-trigger" id="eb-UNSC">')
html = html.replace('<!-- AIPPM -->\n                    <div class="eb-group animate-trigger">', '<!-- AIPPM -->\n                    <div class="eb-group animate-trigger" id="eb-AIPPM">')
html = html.replace('<!-- GDWC -->\n                    <div class="eb-group animate-trigger">', '<!-- GDWC -->\n                    <div class="eb-group animate-trigger" id="eb-GDWC">')
html = html.replace('<!-- UNODC -->\n                    <div class="eb-group animate-trigger">', '<!-- UNODC -->\n                    <div class="eb-group animate-trigger" id="eb-UNODC">')
html = html.replace('<!-- UNHRC -->\n                    <div class="eb-group animate-trigger">', '<!-- UNHRC -->\n                    <div class="eb-group animate-trigger" id="eb-UNHRC">')
html = html.replace('<!-- IAEA -->\n                    <div class="eb-group animate-trigger">', '<!-- IAEA -->\n                    <div class="eb-group animate-trigger" id="eb-IAEA">')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

# 2. Update app.js
with open("app.js", "r", encoding="utf-8") as f:
    js = f.read()

if 'document.getElementById("meet-eb-btn")' not in js:
    js = js.replace('document.getElementById("modal-desc").innerText = desc;', 
                    'document.getElementById("modal-desc").innerText = desc;\n    document.getElementById("meet-eb-btn").href = "#eb-" + title;')

with open("app.js", "w", encoding="utf-8") as f:
    f.write(js)

# 3. Update style.css
with open("style.css", "a", encoding="utf-8") as f:
    f.write("\n.eb-group { scroll-margin-top: 100px; }\n")

print("Added Meet EB feature")
