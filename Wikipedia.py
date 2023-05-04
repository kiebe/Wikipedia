import webbrowser
from tkinter import *
from time import *

'''
В общем это программа которая по запросу в поле ввода ищет статью на Википедии
Если поле ввода будет пустое то будет показана главная страница Википедии
'''

root = Tk()
root.geometry('272x137+300+200')
root.title('Wikipedia')
root.config(bg='#171717')

lb_head = Label(root, text='Wikipedia')
lb_head.config(font=('Arial', 30), bg='#171717', fg='#ffffff')
lb_head.pack()

lb_serch = Label(root, text='Название статьи:')
lb_serch.config(font=('Arial', 10, 'bold'), bg='#171717', fg='#ffffff')
lb_serch.place(x=10 ,y=70)

en_serch = Entry(root, width=20, bg='#6b6b6b', fg='#ffffff')
en_serch.place(x=135 ,y=72)

def serch():
    serch =  en_serch.get()
    webbrowser.open_new_tab('https://ru.wikipedia.org/wiki/'+serch)

btn_serch = Button(root, width=10, command=serch, text='Search')
btn_serch.place(x=10, y=100)


root.mainloop()
