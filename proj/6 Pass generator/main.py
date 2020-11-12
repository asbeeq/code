from tkinter import *
import random, string 	# string - содержить константы: алфавит, последовательность цифр, пунктуацию...
import pyperclip		# для работы с промежуточным хранилищем данных


PADY=5

root=Tk()
root.geometry("400x200")
root.resizable(0,0)
root.title("Генератор паролей")

Label(root, text='Генератор', font='arial 15 bold').pack()
Label(root, text='Длина пароля', font='arial 10 bold').pack()

pass_len = IntVar()
Spinbox(root, from_=8, to_=32, textvariable=pass_len, width=15).pack()
pass_str = StringVar()

def generate():
    password = random.choice(string.ascii_uppercase)+random.choice(string.ascii_lowercase)+random.choice(string.digits)+random.choice(string.punctuation)
    
    for y in range(pass_len.get()-4):
        password += random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    pass_str.set(password)

Button(root, text="С ГЕНЕРИРОВАТЬ ПАРОЛЬ", command=generate).pack(pady=PADY)
Entry(root, textvariable=pass_str).pack()

def Copy_password():
    pyperclip.copy(pass_str.get())

Button(root, text='КОПИРОВАТЬ', command=Copy_password).pack(pady=PADY)

root.mainloop()