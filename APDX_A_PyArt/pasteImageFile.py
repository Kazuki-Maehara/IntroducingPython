from PIL import Image


img = Image.open('./testImage.png')
crop = (30, 70, 300, 200)
croppedImage = img.crop(crop)
print(croppedImage.size)

img.paste(croppedImage, (200, 200))
img.show()
