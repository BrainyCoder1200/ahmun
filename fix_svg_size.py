import re

for svg_file in ["ICONS/AIPPM.svg", "ICONS/UNSC.svg"]:
    try:
        with open(svg_file, "r", encoding="utf-8") as f:
            data = f.read()
        
        # Remove width="X" and height="X" from the first <svg ...> tag
        # Only from the root <svg> tag!
        match = re.search(r'<svg[^>]*>', data)
        if match:
            svg_tag = match.group(0)
            new_tag = re.sub(r'\swidth="[^"]+"', '', svg_tag)
            new_tag = re.sub(r'\sheight="[^"]+"', '', new_tag)
            data = data.replace(svg_tag, new_tag)
            
            with open(svg_file, "w", encoding="utf-8") as f:
                f.write(data)
            print(f"Fixed {svg_file}")
    except Exception as e:
        print(f"Failed {svg_file}: {e}")
