from PIL import Image


img = Image.open('./testImage.png')
crop = (55, 70, 300, 300)
img2 = img.crop(crop)
img2.show()
