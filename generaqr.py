import qrcode
img = qrcode.make('https://github.com/hugo-araya')
type(img)  # qrcode.image.pil.PilImage
img.save("githubharaya.png")