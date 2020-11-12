from tkinter import *
from gtts import gTTS 		# google text-to-speech
from playsound import playsound


root = Tk()
root.geometry('360x300')
root.resizable(0,0)
root.config(bg='white')
root.title('Преобразование текста в голос')

Label(root, text='Текст -> Голос' , font='arial 20 bold', bg='white').pack()
Label(root, text='Введите текст', font='arial 14 bold', bg='white').place(x=20,y=60)

msg = StringVar()

Entry(root, textvariable=msg, width ='45').place(x=20, y=100)

def text_to_speech():
    Message = msg.get()
    print(Message)
    speech = gTTS(Message, lang='ru')
    speech.save('sound.mp3')
    playsound('sound.mp3')

def exit():
    root.destroy()

def reset():
    msg.set("")

Button(root, text="ИГРАТЬ", font='arial 12 bold', command=text_to_speech).place(x=50, y=140)
Button(root, text='ВЫЙТИ', font='arial 12 bold', command=exit).place(x=125,y=140)
Button(root, text='СБРОС', font='arial 12 bold', command=reset).place(x=200, y=140)

root.mainloop()