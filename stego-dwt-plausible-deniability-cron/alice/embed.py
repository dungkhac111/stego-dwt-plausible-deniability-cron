from PIL import Image

KEY = 0x42   # Bob biết – Eve không
END = b"####"

def to_bits(data):
    return ''.join(format(b, '08b') for b in data)

img = Image.open("cover.png").convert("RGB")
pixels = img.load()
w, h = img.size

with open("lh.txt", "rb") as f:
    lh = f.read() + END

with open("hh.txt", "rb") as f:
    hh = bytes([b ^ KEY for b in f.read()]) + END

lh_bits = to_bits(lh)
hh_bits = to_bits(hh)

li = hi = 0

for y in range(h):
    for x in range(w):
        r, g, b = pixels[x, y]

        if li < len(lh_bits):
            r = (r & ~1) | int(lh_bits[li])
            li += 1

        if hi < len(hh_bits):
            b = (b & ~1) | int(hh_bits[hi])
            hi += 1

        pixels[x, y] = (r, g, b)

        if li >= len(lh_bits) and hi >= len(hh_bits):
            img.save("stego.png")
            print("Embedded LH + HH into stego.png")
            exit()

