import qrcode
img = qrcode.make('https://youtu.be/yPYZpwSpKmA?si=MfoMIkzWbj4C2Alf')
type(img)  # qrcode.image.pil.PilImage
img.save("qr1.png")