from PIL import Image
import json

im = Image.open(r"rplace2023.png")
im = im.convert("RGB")
size = im.size

print(im.getpixel((0, 0)))

colors = {}

# Use to turn the RGB values into Hex
def rgb2hex(r, g, b):
    return '{:02x}{:02x}{:02x}'.format(r, g, b)


for y in range(size[1]):
    for x in range(size[0]):
        r, g, b = im.getpixel((x, y))
        color = rgb2hex(r, g, b)
        try:
            colors[str(color)] += 1
        except KeyError:
            colors[str(color)] = 1

with open("colors.json", "w") as f:
    json.dump({k: v for k, v in sorted(colors.items(), key=lambda item: item[1], reverse=True)}, f, indent=4)
