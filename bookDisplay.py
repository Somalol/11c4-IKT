from bookClass import Book
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk

import fileread
import bookModify
import writeNewFile
import addBooks

def logout(root):
    root.destroy()
    import login
    
def fileRead():
        global booksList
        booksList = fileread.fileRead()

def showBooks(listBox):
        fileRead()
        listBox.delete(*listBox.get_children())
        for i in range(len(booksList)):
            choosen = booksList[i]
            listBox.insert("", "end", values=(i+1 ,choosen.title, choosen.publisher, choosen.writer, choosen.pages, choosen.date, choosen.rented))

def bookSearch(search, listBox, isRentedVar, searchInput):
        index = 1
        returnIndex = 0
        listBox.delete(*listBox.get_children())

        isRented = isRentedVar.get()

        if(isRented == 1 and search == ""):
            for i in booksList:
                if i.rented == 'False':
                    listBox.insert("", "end", values=(index ,i.title, i.publisher, i.writer, i.pages, i.date, i.rented))
                    index += 1

        if(isRented == 1):
            for i in booksList:
                if i.title == str(search) and i.rented == 'False':
                    listBox.insert("", "end", values=(index ,i.title, i.publisher, i.writer, i.pages, i.date, i.rented))
                    index += 1
                else:
                    if i.writer == search and i.rented == 'False':
                        listBox.insert("", "end", values=(index ,i.title, i.publisher, i.writer, i.pages, i.date, i.rented))
                        index += 1
                returnIndex += 1
        else:
            for i in booksList:
                if i.title == str(search):
                    listBox.insert("", "end", values=(index ,i.title, i.publisher, i.writer, i.pages, i.date, i.rented))
                    index += 1
                else:
                    if i.writer == search:
                        listBox.insert("", "end", values=(index ,i.title, i.publisher, i.writer, i.pages, i.date, i.rented))
                        index += 1
                returnIndex += 1

        if index == 1 :
            messagebox.showerror(title = "Error", message = "Nincs tal??lat")
            showBooks()

def bookRent(search):
        for i in range(len(booksList)):
            if booksList[i].title == search:
                id = i
                break
            
        choose = booksList[id]
        if choose.rented == "True":
            messagebox.showerror(title="K??lcs??nz??s", message= "Sikertelen k??lcs??nz??s")
        else:
            choose.rented = "True"
            messagebox.showinfo(title="K??lcs??nz??s", message= "Sikeres k??lcs??nz??s") 
            writeNewFile.dataWrite(id , booksList)

def adminPage():
        root = Tk()
        root.title('K??nyv k??lcs??nz??s')

        isRentedVar = tk.IntVar()
        #Table
        label = tk.Label(root, text = "K??nyvek", font=("Times New Roman Baltic", 50)).grid(row = 0, column = 0)

        style1 = ttk.Style()
        style1.configure("Treeview.Heading", background="lightgreen", foreground="gray")

        column_names = ('Pozic????', 'C??m', 'Kiad??' , '??r??', 'Oldalak', 'Megjelen??s ??ve' ,'K??lcs??nz??tt-e')

        listBox = ttk.Treeview(root, columns=column_names)

        for col in column_names:
            listBox.heading(col, text=col)
        
        listBox['show'] = 'headings'
        listBox.grid(row=2, column=0, columnspan=5)
        

        showScores = tk.Button(root, text="K??nyvek megjelen??t??se", width=20, command=lambda: showBooks(listBox))
        quitBtn = tk.Button(root, text="Kijelentkez??s", width=15, command=lambda:logout(root))
        #Table END

        #Search
        searchInput = Entry(root, width = 40, )
        searchButton = Button(root, text="Keres??s", width = 15, command=lambda: bookSearch(searchInput.get(), listBox, isRentedVar, searchInput))
        changeButton = Button(root, text = "M??dos??t??s", width = 15, command = lambda:bookModify.modifyInputWindow())
        rentButton = Button(root, text = "K??lcs??nz??s", width = 15, command = lambda: bookRent(searchInput.get()))
        addBooksBtn = Button(root, text="K??nyv felvitele",width = 15, command = lambda: addBooks.NewBook())

        searchInput.grid(row=0, column=1, columnspan = 2)
        searchInput.place(x= 770, y= 25, height=25, anchor='nw')
        searchButton.grid(row=0, column=2)
        searchButton.place(x= 1040, y= 25, height=25, anchor='nw')

        showScores.grid(row=3, column=0)
        quitBtn.grid(row=3, column= 4)
        changeButton.grid(row = 3, column = 1)
        addBooksBtn.grid(row = 3, column = 2)
        rentButton.grid(row = 3, column = 3)
        

        isRentedButton = tk.Checkbutton(root, text='Csak k??lcs??n??zhet??',variable=isRentedVar, onvalue=1, offvalue=0)
        isRentedButton.grid(row=0, column=4)

        style = ttk.Style(root)
        style.theme_use("winnative")

        fileRead()

def userPage():
        root = Tk()
        root.title('K??nyv k??lcs??nz??s')

        isRentedVar = tk.IntVar()
        #Table
        label = tk.Label(root, text = "K??nyvek", font=("Times New Roman Baltic", 50)).grid(row = 0, column = 0)

        style1 = ttk.Style()
        style1.configure("Treeview.Heading", background="lightgreen", foreground="gray")

        column_names = ('Pozic????', 'C??m', 'Kiad??' , '??r??', 'Oldalak', 'Megjelen??s ??ve' ,'K??lcs??nz??tt-e')

        listBox = ttk.Treeview(root, columns=column_names)

        for col in column_names:
            listBox.heading(col, text=col)

        listBox['show'] = 'headings'
        listBox.grid(row=2, column=0, columnspan=4)
        

        showScores = tk.Button(root, text="K??nyvek megjelen??t??se", width=20, command=lambda: showBooks(listBox))
        quitBtn = tk.Button(root, text="Kijelentkez??s", width=15, command=lambda:logout(root))
        #Table END

        #Search
        searchInput = Entry(root, width = 40, )
        searchButton = Button(root, text="Keres??s", width = 15, command=lambda: bookSearch(searchInput.get(), listBox, isRentedVar, searchInput))
        rentButton = Button(root, text = "K??lcs??nz??s", width = 15, command = lambda: bookRent(searchInput.get()))

        searchInput.grid(row=0, column=1, columnspan = 2)
        searchInput.place(x= 770, y= 25, height=25, anchor='nw')
        searchButton.grid(row=0, column=2)
        searchButton.place(x= 1040, y= 25, height=25, anchor='nw')

        showScores.grid(row=3, column=0)
        quitBtn.grid(row=3, column= 3)
        rentButton.grid(row = 3, column = 2)

        isRentedButton = tk.Checkbutton(root, text='Csak k??lcs??n??zhet??',variable=isRentedVar, onvalue=1, offvalue=0)
        isRentedButton.grid(row=0, column=3)

        style = ttk.Style(root)
        style.theme_use("winnative")

        fileRead()