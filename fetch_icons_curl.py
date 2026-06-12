import subprocess
import os

icons_dir = "ICONS"
if not os.path.exists(icons_dir):
    os.makedirs(icons_dir)

svqs = {
    "UNODC": "https://upload.wikimedia.org/wikipedia/commons/1/12/UNODC_Logo.svg",
    "UNHRC": "https://upload.wikimedia.org/wikipedia/commons/5/52/United_Nations_Human_Rights_Council_Logo.svg",
    "IAEA": "https://upload.wikimedia.org/wikipedia/commons/6/6f/International_Atomic_Energy_Agency_Logo.svg",
}

for name, url in svqs.items():
    file_path = os.path.join(icons_dir, f"{name}.svg")
    cmd = f'curl.exe -s -L -A "Mozilla/5.0" -o "{file_path}" "{url}"'
    result = subprocess.run(cmd, shell=True)
    if result.returncode == 0:
        print(f"Downloaded {name}.svg")
    else:
        print(f"Failed to download {name}.svg")

# Colorize them to gold (#fdc934)
for name in ["UNSC", "UNODC", "UNHRC", "IAEA", "AIPPM"]:
    file_path = os.path.join(icons_dir, f"{name}.svg")
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            data = f.read()
        if "<style>" not in data:
            import re
            data = re.sub(r'(<svg[^>]*>)', r'\1' + "<style> * { fill: #fdc934 !important; } </style>", data, count=1)
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(data)
            print(f"Colorized {name}.svg")
