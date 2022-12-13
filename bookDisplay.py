from bookClass import Book
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
import bookMod

import fileread
import bookModify
import writeNewFile

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
            listBox.insert("", "end", values=(i+1 ,choosen.title, choosen.writer, choosen.pages, choosen.date, choosen.rented))

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
            print("Már kölcsönözve")
        else:
            choose.rented = "True"
            print("Könyv ki kölcsönözve") 
            writeNewFile.dataWrite(id , booksList)
        showBooks()

    def modifyCall(search):
        id = bookSearch(search)
        bookModify.modify(id)

    root = Tk()
    root.title('Könyv kölcsönzés')
    #Table
    label = tk.Label(root, text = "Könyvek", font=("Times New Roman Baltic", 50)).grid(row = 0, column = 0)

    style1 = ttk.Style()
    style1.configure("Treeview.Heading", background="lightgreen", foreground="gray")

    column_names = ('Position', 'Cím','Író', 'Oldalak', 'Megjelenés éve' ,'Kölcsönzött-e')

    listBox = ttk.Treeview(root, columns=column_names)

    listBox.heading("#0", text="Position")
    listBox.heading("Cím", text="Cím")
    listBox.heading("Író", text="Író")
    listBox.heading("Oldalak", text="Oldalak")
    listBox.heading("Megjelenés éve", text="Megjelenés éve")
    listBox.heading("Kölcsönzött-e", text="Kölcsönzött-e")

    for col in column_names:
        listBox.heading(col, text=col)    
    listBox.grid(row=2, column=0, columnspan=5)

    showScores = tk.Button(root, text="Könyvek megjelenítése", width=20, command=showBooks).grid(row=3, column=0)
    closeButton = tk.Button(root, text="Kilépés", width=15, command=quit).grid(row=3, column=1)
    #Table END

    #Search
    searchInput = Entry(root, width = 19)
    searchInput.grid(row=2, column=3)
    searchButton = Button(root, text="Keresés", width = 15, command=lambda: bookSearch(searchInput.get())).grid(row=3, column=2)
    changeButton = Button(root, text = "Módosítás", width = 15, command = lambda:modifyCall(searchInput.get())).grid(row = 3, column = 3)
    rentButton = Button(root, text = "Kölcsönzés", width = 15, command = lambda: bookRent(searchInput.get())).grid(row = 3, column = 4)


    style = ttk.Style(root)
    style.theme_use("winnative")

    fileRead()
    root.mainloop()
ezkellide()
#Ezt ki kell venni, ha login van