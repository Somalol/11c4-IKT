from tkinter import *
from bookClass import Book

mod = Tk()


booksList = []
def fileRead():
    with open("testdata.txt", 'r', encoding = 'utf-8') as f:
        for line in f:
            title,writer,pages,date,rented = line.strip().split(";")
            actual = Book(title, writer, pages, date, rented)
            booksList.append(actual)
fileRead()

def bookRent(id):
    id = id-1
    choose = booksList[id]
    if choose.rented == "True":
        print("Már kölcsönözve")
    else:
        choose.rented = "True"
        print("Könyv ki kölcsönözve")
        with open("testdata.txt", 'r', encoding = 'utf-8') as f:
            data = f.readlines()
            print(data)

        with open("testdata.txt", 'w' ,encoding='utf-8') as f:
            data[id] = booksList[id].title+";"+booksList[id].writer+";"+booksList[id].pages+";"+booksList[id].date+";"+booksList[id].rented+"\n"
            f.writelines(data)






def bookMod(id,id2):
    id = id-1
    id2 = id2
    choose = booksList[id]
    with open("testdata.txt", 'r', encoding = 'utf-8') as f:
        data = f.readlines()
        print(data)

    if id2 == 1:
        choose = booksList[id]      
        choose.title = str(input("Kérem a szöveget: "))
        with open("testdata.txt", 'w' ,encoding='utf-8') as f:
            data[id] = booksList[id].title+";"+booksList[id].writer+";"+booksList[id].pages+";"+booksList[id].date+";"+booksList[id].rented+"\n"
            f.writelines(data)
    if id2 == 2:
        choose = booksList[id]
        choose.writer = str(input("Kérem a szöveget: "))
        with open("testdata.txt", 'w' ,encoding='utf-8') as f:
            data[id] = booksList[id].title+";"+booksList[id].writer+";"+booksList[id].pages+";"+booksList[id].date+";"+booksList[id].rented+"\n"
            f.writelines(data)
    if id2 == 3:
        choose = booksList[id]
        choose.pages = str(input("Kérem a szöveget: "))
        with open("testdata.txt", 'w' ,encoding='utf-8') as f:
            data[id] = booksList[id].title+";"+booksList[id].writer+";"+booksList[id].pages+";"+booksList[id].date+";"+booksList[id].rented+"\n"
            f.writelines(data)
    if id2 == 4:
        choose = booksList[id]
        choose.date = str(input("Kérem a szöveget: "))
        with open("testdata.txt", 'w' ,encoding='utf-8') as f:
            data[id] = booksList[id].title+";"+booksList[id].writer+";"+booksList[id].pages+";"+booksList[id].date+";"+booksList[id].rented+"\n"
            f.writelines(data)

bookMod()

