from tkinter import *
import random


root = Tk()
root.geometry('400x400')
root.resizable(0,0)
root.title('Камень-ножницы-бумага')

Label(root, text='Камень-ножницы-бумага', font='arial 15 bold').pack()

Label(root, text='Напишите: камень, ножницы или бумага', font='arial 13 bold').place(x=25, y=70)
user_take = StringVar()
Entry(root, font='arial 15', textvariable=user_take).place(x=90, y=130)
    
Result = StringVar()

def play():
    comp_pick = random.choice(('камень', 'ножницы', 'бумага'))

    user_pick = user_take.get()
    if user_pick == comp_pick:
        Result.set('Ничья!')
    elif user_pick == 'камень' and comp_pick == 'бумага':
        Result.set('Проиграли, компьютер выбрал бумагу')
    elif user_pick == 'камень' and comp_pick == 'ножницы':
        Result.set('Выйграли, компьютер выбрал ножницы')
    elif user_pick == 'бумага' and comp_pick == 'ножницы':
        Result.set('Проиграли, компьютер выбрал ножницы')
    elif user_pick == 'бумага' and comp_pick == 'камень':
        Result.set('Выйграли, компьютер выбрал камень')
    elif user_pick == 'ножницы' and comp_pick == 'камень':
        Result.set('Проиграли, компьютер выбрал камень')
    elif user_pick == 'ножницы' and comp_pick == 'бумага':
        Result.set('Выйграли, компьютер выбрал бумагу')
    else:
        Result.set('Не правильно: введите - камень, ножницы или бумага')
            
def Reset():
    Result.set("") 
    user_take.set("")

def Exit():
    root.destroy()

Entry(root, font='arial 10 bold', textvariable=Result, width=50).place(x=25, y=250)
Button(root, font='arial 13 bold', text = 'Играть', padx=5, command=play).place(x=170,y=190)
Button(root, font='arial 13 bold', text = 'Сброс', padx=5, command=Reset).place(x=90,y=310)
Button(root, font='arial 13 bold', text = 'Выйти', padx=5, command=Exit).place(x=250,y=310)

root.mainloop()