from bookClass import Book
import fileread
import writeNewFile

from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk

booksList = fileread.fileRead()

def confirmModify(id):
    choosen = booksList[id]

    choosen.title = entTitle.get()
    choosen.publisher = entPublisher.get()
    choosen.writer = entWriter.get()
    choosen.pages = entPages.get()
    choosen.date = entDate.get()
    choosen.rented = entRented.get()

    writeNewFile.dataWrite(id , booksList)

def modify(id):
    global entTitle
    global entPublisher
    global entWriter
    global entPages
    global entDate
    global entRented

    choosen = booksList[id]

    lst = [("cím", choosen.title), 
    ("kiadó", choosen.publisher), 
    ("Író", choosen.writer), 
    ("Oldalak száma", choosen.pages),
    ( "Megjelenési dátum", choosen.date), 
    ("Kölcsönzött-e", choosen.rented)]

    total_rows = len(lst)
    total_columns = len(lst[0])

    modRoot = Toplevel()
    modRoot.title("Modify")
    #Lablek
    labTitle = Label(modRoot, text=lst[0][0]).grid(column=0, row=0, columnspan= 2)
    labPublisher = Label(modRoot, text=lst[1][0]).grid(column=0, row=1, columnspan= 2)
    labWriter = Label(modRoot, text=lst[2][0]).grid(column=0, row=2, columnspan= 2)
    labPages = Label(modRoot, text=lst[3][0]).grid(column=0, row=3, columnspan= 2)
    labDate = Label(modRoot, text=lst[4][0]).grid(column=0, row=4, columnspan= 2)
    labRented = Label(modRoot, text=lst[5][0]).grid(column=0, row=5, columnspan= 2)
    #Entry-k
    entTitle = Entry(modRoot)
    entPublisher = Entry(modRoot)
    entWriter = Entry(modRoot)
    entPages = Entry(modRoot)
    entDate = Entry(modRoot)
    entRented = Entry(modRoot)

    entTitle.grid(column=2, row=0, columnspan= 2)
    entPublisher.grid(column=2, row=1, columnspan= 2)
    entWriter.grid(column=2, row=2, columnspan= 2)
    entPages.grid(column=2, row=3, columnspan= 2)
    entDate.grid(column=2, row=4, columnspan= 2)
    entRented.grid(column=2, row=5, columnspan= 2)

    entTitle.insert(END, lst[0][1])
    entPublisher.insert(END, lst[1][1])
    entWriter.insert(END, lst[2][1])
    entPages.insert(END, lst[3][1])
    entDate.insert(END, lst[4][1])
    entRented.insert(END, lst[5][1])

    Conf = Button(modRoot, text="Bevitel", command=lambda: confirmModify(id))
    Conf.grid(column=0 , row=6, columnspan=2)

    closeButton = Button(modRoot, text="Close", width=15, command=modRoot.destroy)
    closeButton.grid(row=6, column=2, columnspan=2)
    modRoot.mainloop