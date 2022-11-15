from bookClass import Book

booksList = []
def fileRead():
    with open("file.txt", 'r', encoding = 'utf-8') as f:
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
        with open("file.txt", 'r', encoding = 'utf-8') as f:
            data = f.readlines()
            print(data)

        with open("file.txt", 'w' ,encoding='utf-8') as f:
            data[id] = booksList[id].title+";"+booksList[id].writer+";"+booksList[id].pages+";"+booksList[id].date+";"+booksList[id].rented+"\n"
            f.writelines(data)

bookRent(4)