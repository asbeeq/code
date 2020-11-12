from tkinter import *
import datetime
import time
import winsound


def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")   # форматирует время
        date = current_time.strftime("%d/%m/%Y")  # форматирует дату
        print("Установленное время:", date)
        print(now)
        if now == set_alarm_timer:
            print("Подъем!")
            winsound.PlaySound("sound1.wav", winsound.SND_ASYNC)
            break

def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)

root = Tk()
root.title("Будильник")
root.geometry("350x200")


Label(root, text="Час    Мин     Сек", font=70).place(x=130)
Label(root, text="Установить на", fg="blue", font=("Helevetica", 9, "bold")).place(x=10, y=29)

hour = StringVar()
min = StringVar()
sec = StringVar()

Entry(root, textvariable=hour, fg="white", bg="gray", width=4, font=("Helevetica", 14, "bold")).place(x=120, y=30)
Entry(root, textvariable=min, fg="white", bg="gray", width=4, font=("Helevetica", 14, "bold")).place(x=170, y=30)
Entry(root, textvariable=sec, fg="white", bg="gray", width=4, font=("Helevetica", 14, "bold")).place(x=220, y=30)

Button(root, text="Установить", fg="white", bg="green", width=10, font="Arial", command=actual_time).place(x=167, y=70)
Label(root, text="Введите время в 24-ом формате!", fg="white", bg="black").place(x=67, y=120)

root.mainloop()