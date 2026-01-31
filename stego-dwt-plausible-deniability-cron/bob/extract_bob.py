from PIL import Image

KEY = 0x42
END = b"####"

import sys


img_path = sys.argv[1]
img = Image.open(img_path)
pixels = img.load()
w, h = img.size

bits_r = ""
bits_b = ""

for y in range(h):
    for x in range(w):
        r, g, b = pixels[x, y]
        bits_r += str(r & 1)
        bits_b += str(b & 1)

def bits_to_msg(bits, xor=False):
    data = []
    for i in range(0, len(bits), 8):
        byte = bits[i:i+8]
        if len(byte) < 8:
            break
        data.append(int(byte, 2))
    raw = bytes(data)
    if xor:
        raw = bytes([b ^ KEY for b in raw])
    return raw.split(END)[0]

lh = bits_to_msg(bits_r)
hh = bits_to_msg(bits_b, xor=True)

print(lh[:200].decode(errors="ignore"))
print(hh[:200].decode(errors="ignore"))


