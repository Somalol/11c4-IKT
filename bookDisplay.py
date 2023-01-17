from bookClass import Book
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
import login

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
            messagebox.showerror(title = "Error", message = "Nincs találat")
            showBooks()

def bookRent(search):
        for i in range(len(booksList)):
            if booksList[i].title == search:
                id = i
                break
            
        choose = booksList[id]
        if choose.rented == "True":
            messagebox.showerror(title="Kölcsönzés", message= "Sikertelen kölcsönzés")
        else:
            choose.rented = "True"
            messagebox.showinfo(title="Kölcsönzés", message= "Sikeres kölcsönzés") 
            writeNewFile.dataWrite(id , booksList)

def adminPage():
        root = Tk()
        root.title('Könyv kölcsönzés')

        isRentedVar = tk.IntVar()
        #Table
        label = tk.Label(root, text = "Könyvek", font=("Times New Roman Baltic", 50)).grid(row = 0, column = 0)

        style1 = ttk.Style()
        style1.configure("Treeview.Heading", background="lightgreen", foreground="gray")

        column_names = ('Pozicíó', 'Cím', 'Kiadó' , 'Író', 'Oldalak', 'Megjelenés éve' ,'Kölcsönzött-e')

        listBox = ttk.Treeview(root, columns=column_names)

        for col in column_names:
            listBox.heading(col, text=col)
        
        listBox['show'] = 'headings'
        listBox.grid(row=2, column=0, columnspan=5)
        

        showScores = tk.Button(root, text="Könyvek megjelenítése", width=20, command=lambda: showBooks(listBox))
        quitBtn = tk.Button(root, text="Kijelentkezés", width=15, command=lambda:logout(root))
        #Table END

        #Search
        searchInput = Entry(root, width = 40, )
        searchButton = Button(root, text="Keresés", width = 15, command=lambda: bookSearch(searchInput.get(), listBox, isRentedVar, searchInput))
        changeButton = Button(root, text = "Módosítás", width = 15, command = lambda:bookModify.modifyInputWindow())
        rentButton = Button(root, text = "Kölcsönzés", width = 15, command = lambda: bookRent(searchInput.get()))
        addBooksBtn = Button(root, text="Könyv felvitele",width = 15, command = lambda: addBooks.NewBook())

        searchInput.grid(row=0, column=1, columnspan = 2)
        searchInput.place(x= 770, y= 25, height=25, anchor='nw')
        searchButton.grid(row=0, column=2)
        searchButton.place(x= 1040, y= 25, height=25, anchor='nw')

        showScores.grid(row=3, column=0)
        quitBtn.grid(row=3, column= 4)
        changeButton.grid(row = 3, column = 1)
        addBooksBtn.grid(row = 3, column = 2)
        rentButton.grid(row = 3, column = 3)
        

        isRentedButton = tk.Checkbutton(root, text='Csak kölcsönözhető',variable=isRentedVar, onvalue=1, offvalue=0)
        isRentedButton.grid(row=0, column=4)

        style = ttk.Style(root)
        style.theme_use("winnative")

        fileRead()

def userPage():
        root = Tk()
        root.title('Könyv kölcsönzés')

        isRentedVar = tk.IntVar()
        #Table
        label = tk.Label(root, text = "Könyvek", font=("Times New Roman Baltic", 50)).grid(row = 0, column = 0)

        style1 = ttk.Style()
        style1.configure("Treeview.Heading", background="lightgreen", foreground="gray")

        column_names = ('Pozicíó', 'Cím', 'Kiadó' , 'Író', 'Oldalak', 'Megjelenés éve' ,'Kölcsönzött-e')

        listBox = ttk.Treeview(root, columns=column_names)

        for col in column_names:
            listBox.heading(col, text=col)

        listBox['show'] = 'headings'
        listBox.grid(row=2, column=0, columnspan=4)
        

        showScores = tk.Button(root, text="Könyvek megjelenítése", width=20, command=lambda: showBooks(listBox))
        quitBtn = tk.Button(root, text="Kijelentkezés", width=15, command=lambda:logout(root))
        #Table END

        #User
        UserOptions = StringVar()
        UserOptions.set(login.benev)

        options = [
            login.benev,
            "Könyveim",
            "Kijelentkezés"
        ]

        drop = OptionMenu(root, UserOptions, *options)
        drop.grid(row=0, column=4)
        drop.place(anchor = "nw")

        #Search
        searchInput = Entry(root, width = 40)
        searchButton = Button(root, text="Keresés", width = 15, command=lambda: bookSearch(searchInput.get(), listBox, isRentedVar, searchInput))
        rentButton = Button(root, text = "Kölcsönzés", width = 15, command = lambda: bookRent(searchInput.get()))

        searchInput.grid(row=0, column=1, columnspan = 2)
        searchInput.place(x= 770, y= 25, height=25, anchor='nw')
        searchButton.grid(row=0, column=2)
        searchButton.place(x= 1040, y= 25, height=25, anchor='nw')

        showScores.grid(row=3, column=0)
        quitBtn.grid(row=3, column= 3)
        rentButton.grid(row = 3, column = 2)

        isRentedButton = tk.Checkbutton(root, text='Csak kölcsönözhető',variable=isRentedVar, onvalue=1, offvalue=0)
        isRentedButton.grid(row=0, column=3)

        style = ttk.Style(root)
        style.theme_use("winnative")

        fileRead()