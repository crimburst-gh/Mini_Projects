# 1st Step is to install the library of qr code
# Type in terminal (pip install qrcode[pil])

import qrcode

url = input("Enter the URL: ").strip()
file_path = "C:\\Users\\Clarence\\OneDrive\\Desktop\\QRCode.png"

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()
img.save(file_path)

print("QR Code was generated!")
