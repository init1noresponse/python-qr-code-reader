from PIL import ImageGrab

from pyzbar.pyzbar import decode
from PIL import Image

img = ImageGrab.grabclipboard()

if img is None:
    print('No image in clipboard!\n')
else: 
    data = decode(img)
    print(data)
