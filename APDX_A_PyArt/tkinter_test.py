import tkinter
from PIL import Image, ImageTk


main = tkinter.Tk()
img = Image.open('./testImage.png')
tking = ImageTk.PhotoImage(img)
print(type(tking))
tkinter.Label(main, image=tking).pack()
main.mainloop()
