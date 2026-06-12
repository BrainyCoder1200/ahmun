import os
import re

file_path = "ICONS/AIPPM.svg"
if os.path.exists(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        data = f.read()
    if "<style>" not in data:
        data = re.sub(r'(<svg[^>]*>)', r'\1' + "<style> * { fill: #fdc934 !important; stroke: #fdc934 !important; } </style>", data, count=1)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(data)
        print("Colorized AIPPM.svg")
