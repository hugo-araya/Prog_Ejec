import qrcode
img = qrcode.make('https://youtu.be/d37Izzyll8E')
type(img)  # qrcode.image.pil.PilImage
img.save("envases.png")