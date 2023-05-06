'''
!!!Программа работает только на версии питона 3.6.9!!!
Так же надо уствновить custom tkinter: pip install customtkinter/pip3 install customtkinter
'''

import webbrowser
import customtkinter

customtkinter.set_appearance_mode("System")  
customtkinter.set_default_color_theme("green") 

root = customtkinter.CTk() 
root.geometry("272x130")
root.title('Wikipedia')

lb_head = customtkinter.CTkLabel(root, text='Wikipedia')
lb_head.configure(font=('Arial', 30))
lb_head.pack()

lb_serch = customtkinter.CTkLabel(root, text='Название статьи:')
lb_serch.configure(font=('Arial', 15,))
lb_serch.place(x=10 ,y=52)

search_en = customtkinter.CTkEntry(root, width=135)
search_en.place(x=135, y=52)


def search():
    search =  search_en.get()
    webbrowser.open_new_tab('https://ru.wikipedia.org/wiki/'+search)

button = customtkinter.CTkButton(root, text="search", command=search)
button.place(x=10, y=93)
root.mainloop()
