booksList = []
def fileRead():
    with open("file.txt", 'r', encoding = 'utf-8') as f:
        actual = {}
        for line in f:
            title,writer,pages,date,rented = line.strip().split(";")
            actual = {
                "Title": title,
                "Writer" : writer,
                "Pages" : pages,
                "Date" : date,
                "Status" :rented
            }
            booksList.append(actual)
fileRead()

def bookRent(id):
    id = id-1
    choose = booksList[id]
    if choose["Status"] == "True":
        print("Már kölcsönözve")
    else:
        choose["Status"] = "True"
        print("Könyv ki kölcsönözve")
        with open("file.txt", 'r', encoding = 'utf-8') as f:
            data = f.readlines()
            print(data)

        with open("file.txt", 'w' ,encoding='utf-8') as f:
            data[id] = booksList[id]["Title"]+";"+booksList[id]["Writer"]+";"+booksList[id]["Pages"]+";"+booksList[id]["Date"]+";"+booksList[id]["Status"]+"\n"
            f.writelines(data)

bookRent(10)