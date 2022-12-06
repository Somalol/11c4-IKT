from bookClass import Book
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
import bookMod

def ezkellide():
    
    booksList = []

    def fileRead():
        with open("books.txt", 'r', encoding = 'utf-8') as f:
            for line in f:
                title, publisher, writer, pages,date, rented = line.strip().split(";")
                actual = Book(title, publisher, writer, pages, date, rented)
                booksList.append(actual)

    def showBooks():
        fileRead()
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
                return(booksList.index(i))
            else:
                if i.writer == search:
                    listBox.insert("", "end", values=(index ,i.title, i.writer, i.pages, i.date, i.rented))
                    index += 1
                    return(booksList.index(i))
                elif i.rented == search:
                    listBox.insert("", "end", values=(index,i.title, i.writer, i.pages, i.date, i.rented))
                    index += 1
                    return(booksList.index(i))

        if index == 1 :
            messagebox.showerror(title = "Error", message = "Nincs találat")
            showBooks()

    def bookRent(search):
        id = bookSearch(search)
        if(booksList[id].rented == "False"):
            booksList[id].rented = "True"
            messagebox.showinfo(title = "Siker", message = "Sikeresen kikölcsönözte a kívánt könyvet!")
        else:
            messagebox.showerror(title = "Error", message = "A könyv már ki van kölcsönözve!")
        data = booksList[id].title+";"+booksList[id].publisher+";"+booksList[id].writer+";"+booksList[id].pages+";"+booksList[id].date+";"+booksList[id].rented+"\n"
        modDone(data, id)
        showBooks()

    def bookMod(search):
        id = bookSearch(search)
        mod = Toplevel(root)
        mod.title("Adatmódosítás")

        lab1 = Label(mod, text="Cím:").grid(column=0, row=0)
        lab2 = Label(mod, text="Kiadó:").grid(column=0, row=1)
        lab3 = Label(mod, text="Író:").grid(column=0, row=2)
        lab4 = Label(mod, text="Oldalak:").grid(column=0, row=3)
        lab5 = Label(mod, text="Megjelenési idő:").grid(column=0, row=4)
        ent1 = Entry(mod)
        ent2 = Entry(mod)
        ent3 = Entry(mod)
        ent4 = Entry(mod)
        ent5 = Entry(mod)
        ent1.grid(column=1, row=0)
        ent2.grid(column=1, row=1)
        ent3.grid(column=1, row=2)
        ent4.grid(column=1, row=3)
        ent5.grid(column=1, row=4)

        #Az adat átírás nem jó még
        data = ent1.get()+";"+ent2.get()+";"+ent3.get()+";"+ent4.get()+";"+ent5.get()+";"+booksList[id].rented+"\n"
        confirm = Button(mod, text="Bevitel", command=lambda:modDone(data, id)) .grid(column=0, row=5, columnspan=2)
    
    def modDone(modifiedData, id):
        with open("books.txt", 'r', encoding = 'utf-8') as f:
            data = f.readlines()
        data[id] = modifiedData
        with open("books.txt", 'w', encoding = 'utf-8') as f:
            f.writelines(data)
        messagebox.showinfo(title = "Siker!", message = "Sikeres adatmódosítás")

    root = Tk()
    root.title('Könyv kölcsönzés')
    #Table
    label = tk.Label(root, text = "Könyvek", font = ("Arial", 30)).grid(row = 0, column = 0)
    cols = ('Position', 'Cím','Író', 'Oldalak', 'Megjelenés éve' ,'Kölcsönzött-e')
    listBox = ttk.Treeview(root, columns=cols, show='headings')

    for col in cols:
        listBox.heading(col, text=col)    
    listBox.grid(row=2, column=0, columnspan=2)

    showScores = tk.Button(root, text="Könyvek megjelenítése", width=20, command=showBooks).grid(row=3, column=0)
    closeButton = tk.Button(root, text="Kilépés", width=15, command=quit).grid(row=3, column=1)
    #Table END

    #Search
    searchInput = Entry(root, width = 19)
    searchInput.grid(row=2, column=3)
    searchButton = Button(root, text="Keresés", width = 15, command=lambda: bookSearch(searchInput.get())).grid(row=3, column=2)
    changeButton = Button(root, text = "Módosítás", width = 15, command = lambda: bookMod(searchInput.get())).grid(row = 3, column = 3)
    rentButton = Button(root, text = "Kölcsönzés", width = 15, command = lambda: bookRent(searchInput.get())).grid(row = 3, column = 4)

    root.mainloop()
ezkellide()
#Ezt ki kell venni, ha login van