from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import random

numbers = '1234567890'
base = ['', '', '']
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'


def get_entry(list0):
    list0[0] = entry1.get()
    if list0[0] not in numbers or list0[0] == '':
        messagebox.showerror("Error", "Введите ЦИФРУ в 1ую ячейку")
        return None
    elif 0 > int(list0[0]) > 10:
        messagebox.showerror("Error", "Введите ЦИФРУ в 1ую ячейку")
        return None
    list0[1] = entry2.get()
    if list0[1] not in numbers or list0[1] == '':
        messagebox.showerror("Error", "Введите ЦИФРУ в 2ую ячейку")
        return None
    elif 0 > int(list0[1]) > 10:
        messagebox.showerror("Error", "Введите ЦИФРУ в 2ую ячейку")
        return None
    list0[2] = entry3.get()
    if list0[2] not in numbers or list0[2] == '':
        messagebox.showerror("Error", "Введите ЦИФРУ в 3ую ячейку")
        return None
    elif 0 > int(list0[2]) > 10:
        messagebox.showerror("Error", "Введите ЦИФРУ в 3ую ячейку")
        return None


def keygen(al, list0):
    string = ''
    list1 = []
    counter = 5
    er = 1
    for i in range(len(list0)):
        if list0[i].isdigit() and 10 > int(list0[i]) > 0:
            er = 0
        else:
            return None
    if er == 0:
        for i in range(counter):
            x = random.randint(0, len(al) - 1)
            string += al[x]
            list1.append(x)
        string += '-'
        x = 1
        for i in range(counter - 1):
            if i == 3:
                string = string[:-1]
                lbl.configure(text=string)
                return None
            for j in range(counter - i - 1):
                list1[j] += int(list0[i]) * x
                if list1[j] >= 36:
                    list1[j] -= 36
                string += al[list1[j]]
            x *= -1
            string += '-'
            list1.pop(counter - 1 - i)
    else:
        lbl.configure(text=string)


root = Tk()
root.title("Лабораьорная Работа №3")
root.resizable(False, False)
img = Image.open('game_art.png').resize((650, 420))
bg = ImageTk.PhotoImage(img)

root.geometry("650x420")

label = Label(root, image=bg)
label.place(x=0, y=0)

entry1 = Entry(root, font=("Impact", 24), justify=CENTER)
entry1.place(x=275, y=50, width=24)

entry2 = Entry(root, font=("Impact", 24), justify=CENTER)
entry2.place(x=325, y=50, width=24)

entry3 = Entry(root, font=("Impact", 24), justify=CENTER)
entry3.place(x=375, y=50, width=24)

lbl = Label(root, text='', font=("Impact", 18))
lbl.place(x=235, y=150)

btn = Button(text='Ввод', command=lambda: [get_entry(base), keygen(alphabet, base)], font=("Impact", 12))
btn.place(x=315, y=100)


root.mainloop()
