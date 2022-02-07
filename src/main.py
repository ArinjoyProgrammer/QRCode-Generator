import pyqrcode
import png
from pyqrcode import QRCode


def qrCodeGen():
    user = input("Type/Paste a Link or a Text to create a QRCode: ")
    print(f"A QRCode has been created named {user}")

    image = pyqrcode.create(user)

    image.png(f'{user}_QRCode.png', scale=8)

qrCodeGen()
