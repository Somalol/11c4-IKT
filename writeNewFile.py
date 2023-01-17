from bookClass import Book
from tkinter import messagebox

def dataWrite(id, list):    
    with open("books.txt", 'r', encoding = 'utf-8') as f:
            data = f.readlines()
    with open("books.txt", 'w' ,encoding='utf-8') as f:
            data[id] = list[id].title+";"+list[id].publisher+";"+list[id].writer+";"+list[id].pages+";"+list[id].date+";"+list[id].rented+"\n"
            f.writelines(data)

def deleteRecords(id):
        with open("books.txt", "r", encoding= 'utf-8') as file:
                data = file.readlines()

        with open("books.txt", "w", encoding= 'utf-8') as file:
                for i in range(len(data)):
                        if i != id:
                                file.writelines(str(data[i]))
                messagebox.showinfo(title="Kölcsönzés", message= "Sikeres törlés")

def addRecord(title, publisher,writer,pages, date, rented):
        with open("books.txt", "a", encoding= 'utf-8') as file:
                file.write("\n" + title + ";" + publisher + ";" + writer + ";" + pages +";"+ date +";" + rented)