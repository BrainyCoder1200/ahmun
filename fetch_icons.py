import urllib.request
import os

icons_dir = "ICONS"
if not os.path.exists(icons_dir):
    os.makedirs(icons_dir)

svqs = {
    "UNSC": "https://upload.wikimedia.org/wikipedia/commons/e/ee/UN_emblem_blue.svg",
    "UNODC": "https://upload.wikimedia.org/wikipedia/commons/1/12/UNODC_Logo.svg",
    "UNHRC": "https://upload.wikimedia.org/wikipedia/commons/5/52/United_Nations_Human_Rights_Council_Logo.svg",
    "IAEA": "https://upload.wikimedia.org/wikipedia/commons/6/6f/International_Atomic_Energy_Agency_Logo.svg",
    "AIPPM": "https://upload.wikimedia.org/wikipedia/commons/5/55/Emblem_of_India.svg",
    "GDWC": "https://upload.wikimedia.org/wikipedia/commons/b/b2/NATO_star.svg"
}

for name, url in svqs.items():
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            svg_data = response.read().decode('utf-8')
            
            # Inject CSS to force fill to gold
            style_tag = "<style> * { fill: #fdc934 !important; } </style>"
            if "<svg" in svg_data:
                svg_data = svg_data.replace(">", ">" + style_tag, 1) # Insert right after the first > (which is typically <svg...>)
                # Well, actually, replacing the first > might break if there's an XML declaration like <?xml version="1.0"?>
            
            # A safer way to inject style into SVG:
            # Find <svg ... >
            import re
            svg_data = re.sub(r'(<svg[^>]*>)', r'\1' + style_tag, svg_data, count=1)

            file_path = os.path.join(icons_dir, f"{name}.svg")
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(svg_data)
            print(f"Successfully downloaded and colorized {name}.svg")
    except Exception as e:
        print(f"Failed to download {name}: {e}")
