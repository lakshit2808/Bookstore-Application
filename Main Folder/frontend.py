from tkinter import *
from backend import Database

database = Database()
def viewcmd():
    list_box.delete(0 ,END)
    for i in database.view():
        list_box.insert(END , i)

def searchcmd():
    list_box.delete(0,END)
    for i in database.search(et1.get() ,et2.get() ,e3.get() ,et4.get()):
        print(list_box.insert(END , i))

def insertcmd():
    database.insert(et1.get() ,et2.get() ,e3.get() ,et4.get())
    list_box.delete(0, END)
    list_box.insert(END , (et1.get() ,et2.get() ,e3.get() ,et4.get()))

def deletecmd():
    database.delete(et4.get())

def updatecmd():
    database.update(et1.get() ,et2.get() ,e3.get() ,et4.get())
window = Tk()
window.wm_title(" My Books ")
l1 = Label(window , text="Title")
l1.grid(row=0 , column=0)

l2 = Label(window , text="Author")
l2.grid(row=0 , column=2)

l3 = Label(window , text="Year")
l3.grid(row=1 , column=0)

l4 = Label(window , text="isbn")
l4.grid(row=1 , column=2)


et1 = StringVar()
e1 = Entry(window , textvariable=et1)
e1.grid(row=0 , column=1)

et2 = StringVar()
e2 = Entry(window , textvariable=et2)
e2.grid(row=0 , column=3)

et3 = StringVar()
e3 = Entry(window , textvariable=et3)
e3.grid(row=1 , column=1)

et4 = StringVar()
e4 = Entry(window , textvariable=et4)
e4.grid(row=1 , column=3)

list_box = Listbox(window , height=20 , width=50)
list_box.grid(row=2 , column=0)

srl = Scrollbar(window)
srl.grid(row = 1 , column = 1  , rowspan = 6)

list_box.configure(yscrollcommand = srl.set)
srl.configure(command = list_box.yview)

b1 = Button(window , text = "View All" , width = 12 , command = viewcmd )
b1.grid(row = 2 , column =3)

b2 = Button(window , text = "Search" , width = 12 , command = searchcmd)
b2.grid(row = 3 , column =3)

b3 = Button(window , text = "Add New" , width = 12, command = insertcmd)
b3.grid(row = 4 , column =3)

b4 = Button(window , text = "Update" , width = 12 , command = updatecmd)
b4.grid(row = 5 , column =3)

b5 = Button(window , text = "Delete" , width = 12 , command = deletecmd)
b5.grid(row = 6 , column =3)

b6 = Button(window , text = "Close" , width = 12 , command = window.destroy)
b6.grid(row = 7 , column =3)

window.mainloop()