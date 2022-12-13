from bookClass import Book
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk

import fileread
import bookModify
import writeNewFile

def ezkellide():

    def fileRead():
        global booksList
        booksList = fileread.fileRead()

    def showBooks():
        fileRead()
        listBox.delete(*listBox.get_children())
        for i in range(len(booksList)):
            choosen = booksList[i]
            listBox.insert("", "end", values=(i+1 ,choosen.title, choosen.publisher, choosen.writer, choosen.pages, choosen.date, choosen.rented))

    def bookSearch(search):
        index = 1
        returnIndex = 0
        listBox.delete(*listBox.get_children())

        for i in booksList:
            if i.title == str(search):
                listBox.insert("", "end", values=(index ,i.title, i.writer, i.pages, i.date, i.rented))
                index += 1
                return(returnIndex)
            else:
                if i.writer == search:
                    listBox.insert("", "end", values=(index ,i.title, i.writer, i.pages, i.date, i.rented))
                    index += 1
                    return(returnIndex)
                elif i.rented == search:
                    listBox.insert("", "end", values=(index,i.title, i.writer, i.pages, i.date, i.rented))
                    index += 1
                    return(returnIndex)
            returnIndex += 1

        if index == 1 :
            messagebox.showerror(title = "Error", message = "Nincs találat")
            showBooks()

    def bookRent(search):
        id = bookSearch(search)
        choose = booksList[id]
        if choose.rented == "True":
            messagebox.showerror(title="Kölcsönzés", message= "Sikertelen kölcsönzés")
        else:
            choose.rented = "True"
            messagebox.showinfo(title="Kölcsönzés", message= "Sikeres kölcsönzés") 
            writeNewFile.dataWrite(id , booksList)
            bookSearch(search)

    root = Tk()
    root.title('Könyv kölcsönzés')
    #Table
    label = tk.Label(root, text = "Könyvek", font=("Times New Roman Baltic", 50)).grid(row = 0, column = 0)

    style1 = ttk.Style()
    style1.configure("Treeview.Heading", background="lightgreen", foreground="gray")

    column_names = ('Pozicíó', 'Cím', 'Kiadó' , 'Író', 'Oldalak', 'Megjelenés éve' ,'Kölcsönzött-e')

    listBox = ttk.Treeview(root, columns=column_names)

    for col in column_names:
        listBox.heading(col, text=col)    
    listBox.grid(row=2, column=0, columnspan=4)

    showScores = tk.Button(root, text="Könyvek megjelenítése", width=20, command=showBooks)
    closeButton = tk.Button(root, text="Kilépés", width=15, command=quit)
    #Table END

    #Search
    searchInput = Entry(root, width = 40, )
    searchButton = Button(root, text="Keresés", width = 15, command=lambda: bookSearch(searchInput.get()))
    changeButton = Button(root, text = "Módosítás", width = 15, command = lambda:bookModify.modifyInputWindow())
    rentButton = Button(root, text = "Kölcsönzés", width = 15, command = lambda: bookRent(searchInput.get()))

    searchInput.grid(row=0, column=1, columnspan = 2)
    searchInput.place(x= 940, y= 25, height=25, anchor='nw')
    searchButton.grid(row=0, column=2)
    searchButton.place(x= 1200, y= 25, height=25, anchor='nw')

    showScores.grid(row=3, column=0)
    closeButton.grid(row=3, column= 3)
    changeButton.grid(row = 3, column = 1)
    rentButton.grid(row = 3, column = 2)

    style = ttk.Style(root)
    style.theme_use("winnative")

    fileRead()
    root.mainloop()
#ezkellide()
#Ezt ki kell venni, ha login van