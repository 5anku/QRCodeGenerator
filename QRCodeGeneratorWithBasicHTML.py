import qrcode

name = "Aravind Pradeep Nair"
email = "aravind.p.nair@gmail.com"
phone = "1234567890"

vcard_data = f"BEGIN:VCARD\nVERSION:3.0\nFN:{name}\nEMAIL:{email}\nTEL:{phone}\nEND:VCARD"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(vcard_data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

img.save("business_card_qr.png")