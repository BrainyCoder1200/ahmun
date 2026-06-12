from PIL import Image
import sys

def get_colors(image_path):
    try:
        img = Image.open(image_path)
        img = img.convert('RGBA')
        colors = img.getcolors(maxcolors=1000000)
        
        # Sort by frequency
        sorted_colors = sorted(colors, key=lambda t: t[0], reverse=True)
        
        print(f"Top colors in {image_path}:")
        for count, color in sorted_colors[:20]:
            if color[3] > 0: # Ignore fully transparent
                hex_color = '#{:02x}{:02x}{:02x}'.format(color[0], color[1], color[2])
                print(f"{hex_color} - rgb({color[0]}, {color[1]}, {color[2]}) - Count: {count}")
    except Exception as e:
        print(f"Error: {e}")

get_colors("ICONS/ahmunlogo-removebg-preview.png")
