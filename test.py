import qrcode

filename = f"url.png"
# генерируем qr-код
img = qrcode.make("http://80.78.240.58:1337/auth")
img.save(f"url.png")
# Привязываем QR код к пользовате