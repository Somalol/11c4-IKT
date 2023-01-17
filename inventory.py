from tkinter import *
import tkinter as tk
from tkinter import ttk
import fileread
import writeNewFile

booksList = []

def addToInventory(id, username):
    global usernameHere
    usernameHere = username
    booksList = fileread.fileRead()
    if(booksList[id].rented == 'True'):
        with open("inventory.txt", "a", encoding= 'utf-8') as file:
            file.write(id + ";" + username + '\n')

def removeFromInventoryWindow():

    returnWindow = Toplevel()

    lab = Label(returnWindow, text="Könyv címe:")
    lab.pack()
    ent = Entry(returnWindow)
    ent.pack()

    btn = Button(returnWindow, text="Bevitel", command=lambda: removeFromInventory(ent.get()))
    btn.pack()

def removeFromInventory(title):
    with open("inventory.txt", 'r', encoding = 'utf-8') as f:
            data = f.readlines()

    for i in range(len(data)):
        if data[i].title == title:
            invId = i
            break
    
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

def showBooksInventory(listBox):
    with open("inventory.txt", 'r', encoding = 'utf-8') as f:
        data = f.readlines()
    id = 0    
    for i in data:
        if i[1] == usernameHere:
            listBox.delete(*listBox.get_children())
            choosen = booksList[i[0]]
            listBox.insert("", "end", values=(id+1 ,choosen.title, choosen.publisher, choosen.writer, choosen.pages, choosen.date, choosen.rented))
            id += 1

def showInventory():

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

    showBooksInventory(listBox)

    quitBtn = tk.Button(invRoot, text="Kijelentkezés", width=15, command= invRoot.destroy)
    quitBtn.grid(row=3, column= 3)
    returnBtn = Button(invRoot, text="Visszaad", width=15, command = removeFromInventoryWindow)
    returnBtn.grid(row=3, column= 2)

    style = ttk.Style(invRoot)
    style.theme_use("winnative")