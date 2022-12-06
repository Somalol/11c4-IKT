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

def showBooks():
    listBox.delete(*listBox.get_children())
    for i in range(len(booksList)):
        choosen = booksList[i]
        listBox.insert("", "end", values=(i+1 ,choosen.title, choosen.writer, choosen.pages, choosen.date, choosen.rented))

def bookSearch(search):
    index = 1
    listBox.delete(*listBox.get_children())

    for i in booksList:
        if i.title == str(search):
            listBox.insert("", "end", values=(index ,i.title, i.writer, i.pages, i.date, i.rented))
            index += 1
        else:
            if i.writer == search:
                listBox.insert("", "end", values=(index ,i.title, i.writer, i.pages, i.date, i.rented))
                index += 1
            elif i.rented == search:
                listBox.insert("", "end", values=(index,i.title, i.writer, i.pages, i.date, i.rented))
                index += 1

    if index == 1 :
        messagebox.showerror(title = "Error", message = "Nincs találat")
        showBooks()

def modify():

    mod = Toplevel(root)

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
        print(id)
        print(id2)
        id = id-1
        id2 = id2
        choose = booksList[id]
        with open("testdata.txt", 'r', encoding = 'utf-8') as f:
            data = f.readlines()
         
        choose = booksList[id]
        xa = Entry(valt, width= 50, bg= "black", fg= "white", borderwidth= 10, )
        xa.pack()
        xa.insert(0, "Kérem változtatott adatot: ")
            
        def done():
            if id2 == 1:
                choose.title = xa.get()
                with open("testdata.txt", 'w' ,encoding='utf-8') as f:
                    data[id] = booksList[id].title+";"+booksList[id].publisher+";"+booksList[id].writer+";"+booksList[id].pages+";"+booksList[id].date+";"+booksList[id].rented+"\n"
                    f.writelines(data)
            if id2 == 3:
                choose.writer = xa.get() 
                with open("testdata.txt", 'w' ,encoding='utf-8') as f:
                    data[id] = booksList[id].title+";"+booksList[id].publisher+";"+booksList[id].writer+";"+booksList[id].pages+";"+booksList[id].date+";"+booksList[id].rented+"\n"
                    f.writelines(data)
            if id2 == 4: 
                choose.pages = xa.get()
                with open("testdata.txt", 'w' ,encoding='utf-8') as f:
                    data[id] = booksList[id].title+";"+booksList[id].publisher+";"+booksList[id].writer+";"+booksList[id].pages+";"+booksList[id].date+";"+booksList[id].rented+"\n"
                    f.writelines(data)
            if id2 == 2:
                choose.publisher = xa.get()
                with open("testdata.txt", 'w' ,encoding='utf-8') as f:
                    data[id] = booksList[id].title+";"+booksList[id].publisher+";"+booksList[id].writer+";"+booksList[id].pages+";"+booksList[id].date+";"+booksList[id].rented+"\n"
                    f.writelines(data)
            if id2 == 5:
                choose.date = xa.get()
                with open("testdata.txt", 'w' ,encoding='utf-8') as f:
                    data[id] = booksList[id].title+";"+booksList[id].publisher+";"+booksList[id].writer+";"+booksList[id].pages+";"+booksList[id].date+";"+booksList[id].rented+"\n"
                    f.writelines(data)
            lblmo = Label(valt, text="Adat megváltoztatva")
            lblmo.pack()
            btn_mod = Button(valt, text="Bezárás", command= lambda: valt.destroy)
            btn_mod.pack()

                    
        btn_mod = Button(valt, text="Módosítás", command= lambda: done())
        btn_mod.pack()
    btn_at = Button(mod, text="Megkezdés", command=lambda: bookMod())
    btn_at.pack()





root = Tk()
#Table
cols = ('Position', 'Cím','Író', 'Oldalak', 'Megjelenés éve' ,'Kölcsönzött-e')
listBox = ttk.Treeview(root, columns=cols, show='headings')

for col in cols:
    listBox.heading(col, text=col)    
listBox.grid(row=1, column=0, columnspan=2)

showScores = tk.Button(root, text="Show books", width=15, command=showBooks).grid(row=4, column=0)
closeButton = tk.Button(root, text="Close", width=15, command=exit).grid(row=4, column=1)
#Table END

#Search
searchInput = Entry(root)
searchInput.grid(row=4, column=2)
searchBUtton = Button(root, text="Keresés", command=lambda: bookSearch(searchInput.get())).grid(row=4, column=3)

root.mainloop()