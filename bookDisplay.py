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