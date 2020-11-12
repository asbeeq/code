from PIL import Image, ImageTk		# растровая графика
import tkinter as tk
import random


root = tk.Tk()
root.geometry('400x400')
root.title('Рандомный кубик')

tk.Label(root, text="Привет!", fg="green", bg="white", font="Helvetica 16 bold").pack(expand=True)

dice = ['cub1.PNG', 'cub2.PNG', 'cub3.PNG', 'cub4.PNG', 'cub5.PNG', 'cub6.PNG']

img_open = Image.open(random.choice(dice))   # выбрать случайное изображение
img = ImageTk.PhotoImage(img_open)			 # путь до выбранного изображения
label = tk.Label(root, image=img)
label.pack(expand=True)

def roll_dice():
    img_open = Image.open(random.choice(dice))
    img = ImageTk.PhotoImage(img_open)
    label.config(image=img)
    label.image = img

tk.Button(root, text='Бросить кубик', fg='blue', command=roll_dice).pack(expand=True) 	 # с отступом

root.mainloop()