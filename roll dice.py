import tkinter as tk
from PIL import Image, ImageTk
import random

root = tk.Tk()
root.geometry("700x500")
root.configure(bg="yellow")
root.title("ROLL DICE")

a = ["C:/Users/mruty/OneDrive/Desktop/dice faces/dice 1.png","C:/Users/mruty/OneDrive/Desktop/dice faces/dice 2.png","C:/Users/mruty/OneDrive/Desktop/dice faces/dice 3.png",
     "C:/Users/mruty/OneDrive/Desktop/dice faces/dice 4.png","C:/Users/mruty/OneDrive/Desktop/dice faces/dice 5.png","C:/Users/mruty/OneDrive/Desktop/dice faces/dice 6.png"]

#choose the random image from the given list a
b = random.choice(a)

#to load image using PIL
pil_image = Image.open(b)

#resize the image to desired height and width
resize_image = pil_image.resize((300,300))

#convert the pil_image to tkinter compatible photoimage
gui_image = ImageTk.PhotoImage(resize_image)

#add a label to gui_image to display the image
image_label = tk.Label(root,image=gui_image)
image_label.place(x=200,y=50)

def dice_roll():
     image = ImageTk.PhotoImage( Image.open(random.choice(a)).resize((300,300)))
     image_label.configure(image=image)
     image_label.image=image
     image_label.place(x=200,y=50)

#creating a buttton
button = tk.Button(root,text="ROLL",bg="green",fg="white",command=dice_roll,font=("Helvetica", 12),relief="raised")
button.place(x=335,y=0)

root.mainloop()
