from tkinter import *
import writeNewFile

def NewBook():

    addBook = Toplevel() 
    titleVar = StringVar()
    publisherVar = StringVar()
    writerVar = StringVar()
    pagesVar = StringVar()
    dateVar = StringVar()

    titleLab = Label(addBook, text="Cím:").grid(row=0, column=0)
    titleEnt = Entry(addBook, textvariable=titleVar).grid(row=0, column=1)

    publisherLab = Label(addBook, text="Kiadó:").grid(row=1, column=0)
    publisherEnt = Entry(addBook, textvariable=publisherVar).grid(row=1, column=1)

    writerLab = Label(addBook, text="Író:").grid(row=2, column=0)
    writerEnt = Entry(addBook, textvariable=writerVar).grid(row=2, column=1)

    pagesLab = Label(addBook, text="Oldalak:").grid(row=3, column=0)
    pagesEnt = Entry(addBook, textvariable=pagesVar).grid(row=3, column=1)

    dateLab = Label(addBook, text="Megjelenés éve:").grid(row=4, column=0)
    dateEnt = Entry(addBook, textvariable=dateVar).grid(row=4, column=1)

    confBtn = Button(addBook, text="Bevitel", command=lambda: confirm(titleVar.get(), publisherVar.get(), writerVar.get(), pagesVar.get(), dateVar.get(), addBook)).grid(row=5, column=0, columnspan=2)

def confirm(title, publisher,writer,pages, date, addBook):
    addBook.destroy()
    writeNewFile.addRecord(title, publisher,writer,pages, date, "False")



