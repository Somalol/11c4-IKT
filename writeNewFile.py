from bookClass import Book

def dataWrite(id, list):    
    with open("books.txt", 'r', encoding = 'utf-8') as f:
            data = f.readlines()
    with open("books.txt", 'w' ,encoding='utf-8') as f:
            data[id] = list[id].title+";"+list[id].publisher+";"+list[id].writer+";"+list[id].pages+";"+list[id].date+";"+list[id].rented+"\n"
            f.writelines(data)