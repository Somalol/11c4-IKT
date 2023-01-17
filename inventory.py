from tkinter import *
import tkinter as tk
from tkinter import ttk
import fileread
import writeNewFile

booksList = []
ownedBooks = []

def addToInventory(id, username):
    global usernameHere
    usernameHere = username
    with open("inventory.txt", "a", encoding= 'utf-8') as file:
        file.write(str(id) + ";" + username + '\n')

def removeFromInventoryWindow():

    returnWindow = Toplevel()

    lab = Label(returnWindow, text="Könyv címe:")
    lab.pack()
    ent = Entry(returnWindow)
    ent.pack()

    btn = Button(returnWindow, text="Bevitel", command=lambda: removeFromInventory(ent.get()))
    btn.pack()

def removeFromInventory(title):

    ownedBooks.clear()
    with open("books.txt", 'r', encoding = 'utf-8') as f:
        for line in f:
            id, username = line.strip().split(";")
            actual = [id, username]
            ownedBooks.append(actual)

    for i in range(len(ownedBooks)):
        if booksList[ownedBooks[i][0]] == title:
            invId = i
            break

    with open("books.txt", "r", encoding= 'utf-8') as file:
                data = file.readlines()
    
    with open("inventory.txt", "w", encoding= 'utf-8') as file:
                for i in range(len(data)):
                        if i != invId:
                                file.writelines(str(data[i]))

    for i in range(len(booksList)):
        if booksList[i].title == title:
            id = i
            break

    booksList = fileread.fileRead()
    booksList[id].rented == 'False' 
    writeNewFile.dataWrite(id , booksList)

def showBooksInventory(listBox, username):
    booksList = fileread.fileRead()
    with open("inventory.txt", 'r', encoding = 'utf-8') as f:
        for line in f:
            id, username = line.strip().split(";")
            actual = [id, username]
            ownedBooks.append(actual)
    id = 0  

    for ownedBook in ownedBooks:
        if ownedBook[1] == username:
            listBox.delete(*listBox.get_children())
            bookid = ownedBook[0]
            print(bookid)
            choosen = booksList[int(bookid)]
            listBox.insert("", "end", values=(id+1 ,choosen.title, choosen.publisher, choosen.writer, choosen.pages, choosen.date, choosen.rented))
            id += 1

def showInventory(username):

    invRoot = Tk()
    invRoot.title('Saját könyvek')

        #Table
    label = tk.Label(invRoot, text = "Kölcsönzött könyvek", font=("Times New Roman Baltic", 50)).grid(row = 0, column = 0)

    style1 = ttk.Style()
    style1.configure("Treeview.Heading", background="lightgreen", foreground="gray")

    column_names = ('Pozicíó', 'Cím', 'Kiadó' , 'Író', 'Oldalak', 'Megjelenés éve' ,'Kölcsönzött-e')

    listBox = ttk.Treeview(invRoot, columns=column_names)

    for col in column_names:
        listBox.heading(col, text=col)

    listBox['show'] = 'headings'
    listBox.grid(row=2, column=0, columnspan=4)

    showBooksInventory(listBox, username)

    quitBtn = tk.Button(invRoot, text="Kijelentkezés", width=15, command= invRoot.destroy)
    quitBtn.grid(row=3, column= 3)
    returnBtn = Button(invRoot, text="Visszaad", width=15, command = removeFromInventoryWindow)
    returnBtn.grid(row=3, column= 2)

    style = ttk.Style(invRoot)
    style.theme_use("winnative")