from bookClass import Book
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk

booksList = []

def fileRead():
    with open("books.txt", 'r', encoding = 'utf-8') as f:
        for line in f:
            title, publisher, writer, pages, date, rented = line.strip().split(";")

            actual = Book(title, publisher, writer, pages, date, rented)
            
            booksList.append(actual)
fileRead()


def modify():

    mod = Tk()

    mod.title("Adatmódosítás")


    
    lblmo = Label(mod, text="Kérem a változtatandó sor számát")
    lblmo.pack()
    c = Entry(mod, width= 50, bg= "white", fg= "black", borderwidth= 10, )
    c.pack()
    c.insert(0,  "0")  

    
    def callback(selection2):
        valaszt2 = selection2
        global b
        if valaszt2 == "Cím":
            b = 1
        elif valaszt2 == "Író":
            b = 3
        elif valaszt2 == "Oldalszám":
            b = 4
        elif valaszt2 == "Kiadó":
            b = 2
        elif valaszt2 == "Megjelenés éve":
            b = 5
        
            

    variable2 = StringVar(mod)
    variable2.set("Válassza ki a változtatandó adattípust: ")
    w = OptionMenu(mod, variable2, "Cím","Kiadó", "Író", "Oldalszám", "Megjelenés éve", command=callback )
    w.pack()

    def bookMod():
        valt = Toplevel(mod)
        id = int(c.get())
        id2 = b
        id = id-1
        id2 = id2
        choose = booksList[id]
        with open("books.txt", 'r', encoding = 'utf-8') as f:
            data = f.readlines()
         
        choose = booksList[id]
        xa = Entry(valt, width= 50, bg= "black", fg= "white", borderwidth= 10, )
        xa.pack()
        xa.insert(0, "Kérem változtatott adatot: ")
            
        def done():
            if id2 == 1:
                choose.title = xa.get()
                with open("books.txt", 'w' ,encoding='utf-8') as f:
                    data[id] = booksList[id].title+";"+booksList[id].publisher+";"+booksList[id].writer+";"+booksList[id].pages+";"+booksList[id].date+";"+booksList[id].rented+"\n"
                    f.writelines(data)
            if id2 == 3:
                choose.writer = xa.get() 
                with open("books.txt", 'w' ,encoding='utf-8') as f:
                    data[id] = booksList[id].title+";"+booksList[id].publisher+";"+booksList[id].writer+";"+booksList[id].pages+";"+booksList[id].date+";"+booksList[id].rented+"\n"
                    f.writelines(data)
            if id2 == 4: 
                choose.pages = xa.get()
                with open("books.txt", 'w' ,encoding='utf-8') as f:
                    data[id] = booksList[id].title+";"+booksList[id].publisher+";"+booksList[id].writer+";"+booksList[id].pages+";"+booksList[id].date+";"+booksList[id].rented+"\n"
                    f.writelines(data)
            if id2 == 2:
                choose.publisher = xa.get()
                with open("books.txt", 'w' ,encoding='utf-8') as f:
                    data[id] = booksList[id].title+";"+booksList[id].publisher+";"+booksList[id].writer+";"+booksList[id].pages+";"+booksList[id].date+";"+booksList[id].rented+"\n"
                    f.writelines(data)
            if id2 == 5:
                choose.date = xa.get()
                with open("books.txt", 'w' ,encoding='utf-8') as f:
                    data[id] = booksList[id].title+";"+booksList[id].publisher+";"+booksList[id].writer+";"+booksList[id].pages+";"+booksList[id].date+";"+booksList[id].rented+"\n"
                    f.writelines(data)
            lblmo = messagebox.showinfo(title="Adatmódosítás", message="Adat megváltoztatva",)
            lblmo.pack()
            btn_mod = Button(valt, text="Bezárás", command= lambda: valt.destroy)
            btn_mod.pack()

                    
        btn_mod = Button(valt, text="Módosítás", command= lambda: done())
        btn_mod.pack()
    btn_at = Button(mod, text="Megkezdés", command=lambda: bookMod())
    btn_at.pack()



