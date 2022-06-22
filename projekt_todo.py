import tkinter
import tkinter.messagebox

def add(): #dodawanie
    get_task = input_task.get()
    if get_task != "":
        listbox.insert(tkinter.END,get_task)
        input_task.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showinfo(title="", message="You wrote nothing, Add something!")

def delete(): #usuwanie
    try:
        index_taska = listbox.curselection()[0]
        listbox.delete(index_taska)
    except IndexError as Error:
        tkinter.messagebox.showinfo(title="", message="You have to select something!")

#ekran
screen = tkinter.Tk()
screen.title('Lista zadan')
screen.geometry("305x220")

#Ramka
Frame = tkinter.Frame(screen)
Frame.pack()
#interfejs
listbox = tkinter.Listbox(Frame, height=10, width = 40,bg="grey")
listbox.pack(side=tkinter.LEFT)
#scroll
scroll = tkinter.Scrollbar(Frame)
scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)
#input
input_task = tkinter.Entry(screen, width=43,bg="white",)
input_task.pack()

#buttons
button1 = tkinter.Button(screen, text="Add", width=20,bg="silver", command = add)
button2 = tkinter.Button(screen, text="Delete", width=20, bg="silver", command= delete)
button1.pack(side = tkinter.LEFT)
button2.pack(side = tkinter.LEFT)

#config scroll'a zeby przewijal
listbox.config(yscrollcommand=scroll.set)
scroll.config(command = listbox.yview)



screen.mainloop() #start programu





