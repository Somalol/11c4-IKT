from bookClass import Book
from tkinter import *
import tkinter as tk
from tkinter import ttk

booksList = []
def fileRead():
    with open("file.txt", 'r', encoding = 'utf-8') as f:
        for line in f:
            title,writer,pages,date,rented = line.strip().split(";")
            actual = Book(title, writer, pages, date, rented)
            booksList.append(actual)
fileRead()

def showBooks():
    for i in range(len(booksList)):
        choosen = booksList[i]
        listBox.insert("", "end", values=(i+1 ,choosen.title, choosen.writer, choosen.pages, choosen.date, choosen.rented))

root = Tk()
cols = ('Position', 'Író', 'Cím', 'Oldalak', 'Megjelenés éve' 'Kölcsönzött-e')
listBox = ttk.Treeview(root, columns=cols, show='headings')

for col in cols:
    listBox.heading(col, text=col)    
listBox.grid(row=1, column=0, columnspan=2)

showScores = tk.Button(root, text="Show books", width=15, command=showBooks).grid(row=4, column=0)
closeButton = tk.Button(root, text="Close", width=15, command=exit).grid(row=4, column=1)

root.mainloop()