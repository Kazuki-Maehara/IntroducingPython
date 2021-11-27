from PIL import Image


img = Image.open('./testImage.png')
img.save('./testImage.gif', 'GIF')
img_gif = Image.open('./testImage.gif')
print(img_gif.format)
print(img_gif.size)
