from bookClass import Book
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk

def ezkellide():
    booksList = []

    def fileRead():
        with open("books.txt", 'r', encoding = 'utf-8') as f:
            for line in f:
                title, publisher, writer, pages,date, rented = line.strip().split(";")
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

    def bookRent(search):
        listBox.delete(*listBox.get_children())

        for i in booksList:
            if(i.title == str(search)):
                if(i.rented == "False"):
                    i.rented = "True"
                    messagebox.showinfo(title = "Siker", message = "Sikeresen kikölcsönözte a kívánt könyvet!")
                else:
                    messagebox.showerror(title = "Error", message = "A könyv már ki van kölcsönözve!")

        showBooks()


    root = Tk()
    #Table
    label = tk.Label(root, text = "Könyvek", font = ("Arial", 30)).grid(row = 0, column = 0)
    cols = ('Position', 'Cím','Író', 'Oldalak', 'Megjelenés éve' ,'Kölcsönzött-e')
    listBox = ttk.Treeview(root, columns=cols, show='headings')

    for col in cols:
        listBox.heading(col, text=col)    
    listBox.grid(row=2, column=0, columnspan=2)

    showScores = tk.Button(root, text="Show books", width=15, command=showBooks).grid(row=3, column=0)
    closeButton = tk.Button(root, text="Close", width=15, command=exit).grid(row=3, column=1)
    #Table END

    #Search
    searchInput = Entry(root, width = 19)
    searchInput.grid(row=2, column=3)
    searchButton = Button(root, text="Keresés", width = 15, command=lambda: bookSearch(searchInput.get())).grid(row=3, column=2)
    changeButton = Button(root, text = "Módosítás", width = 15).grid(row = 3, column = 3)
    rentButton = Button(root, text = "Kölcsönzés", width = 15, command = lambda: bookRent(searchInput.get())).grid(row = 3, column = 4)

    style = ttk.Style(root)
    style.theme_use("winnative")
    root.mainloop()


ezkellide()
#Ezt ki kell venni, ha login van