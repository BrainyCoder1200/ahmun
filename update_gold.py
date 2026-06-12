import os

css_path = "style.css"
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

css = css.replace("--gold:#ccb17c;", "--gold:#ceac69;")
css = css.replace("--gold-border:rgba(204,177,124,0.25);", "--gold-border:rgba(206,172,105,0.25);")
css = css.replace("--gold-glow:0 0 20px rgba(204,177,124,0.12);", "--gold-glow:0 0 20px rgba(206,172,105,0.12);")
css = css.replace("rgba(204,177,124,.35)", "rgba(206,172,105,.35)")

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)

for name in ["AIPPM", "UNSC"]:
    path = f"ICONS/{name}.svg"
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            data = f.read()
        data = data.replace("#ccb17c", "#ceac69")
        with open(path, "w", encoding="utf-8") as f:
            f.write(data)

print("Updated gold color to #ceac69")
