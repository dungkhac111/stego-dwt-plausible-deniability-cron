from PIL import Image

END = b"####"

img = Image.open("eve.png")
pixels = img.load()
w, h = img.size

bits = ""
for y in range(h):
    for x in range(w):
        r, g, b = pixels[x, y]
        bits += str(r & 1)

data = []
for i in range(0, len(bits), 8):
    byte = bits[i:i+8]
    if len(byte) < 8:
        break
    data.append(int(byte, 2))

msg = bytes(data).split(END)[0]
print("Extracted message:")
print(msg.decode(errors="ignore"))

