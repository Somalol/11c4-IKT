from tkinter import *
from bookClass import Book
from tkinter import ttk

booksList = []

root = Tk()
root.title("Bejelentkezés")
root.configure(bg = "black")

lista = []
booksList = []

lbl_felh = Label(root, text = "Felhasználónév:", bg="black", fg="white")
lbl_felh.grid(row = 1, column = 1)
etr_fhszn = Entry(root, bg = "lightblue", width = 30)
etr_fhszn.grid(row = 2, column = 1)

lbl_jelszo = Label(root, text = "Jelszó: ", bg = "black", fg = "white")
lbl_jelszo.grid(row = 3, column = 1)
etr_jelszo = Entry(root, bg = "lightblue", width = 30)
etr_jelszo.grid(row = 4, column = 1)


with open("loginusers.txt", "r", encoding = "utf-8") as adatok:
    for i in adatok:
        sor = i.strip().split(";")
        lista.append({
            "nev" : str(sor[0]),
            "fhsznev" : str(sor[1]),
            "jelszo" : str(sor[2]),
            "rang" : str(sor[3])
        })

with open("file.txt", 'r', encoding = 'utf-8') as f:
    for line in f:
        title,writer,pages,date,rented = line.strip().split(";")
        actual = Book(title, writer, pages, date, rented)
        booksList.append(actual)


benev = ""
befhsz = ""
bejelszo = ""
betype = ""


def login():
    global befhsz
    global bejelszo
    global benev
    global betype

    befhsz = etr_fhszn.get()
    bejelszo = etr_jelszo.get()

    for i in lista:
        if(i["fhsznev"] == befhsz and i["jelszo"] == bejelszo):
            benev = i["nev"]
            betype = i["rang"]
            if(i["rang"] == "admin"):
                adminpage()
            #elif(i["rang"] == "user"):
            #    userpage()

def adminpage():
    adminpage = Toplevel()
    adminpage.title(str(benev) + ": " + str(betype))
    adminpage.config(bg = "black")

    lbl_tajekoztato = Label(adminpage, bg = "black", fg = "white", text = "Kérem a könyv sorszámát írja be")
    lbl_tajekoztato.grid(row = 0, column = 1)

    etr_bookselect = Entry(adminpage, bg = "lightblue", width = 30)
    etr_bookselect.grid(row = 1, column = 1)

    btn_kolcsonzes = Button(adminpage, text = "Könyv kikölcsönzése", bg = "black", fg = "white", command = lambda:bookRent(int(etr_bookselect.get())))
    btn_kolcsonzes.grid(row = 1, column = 2)   

    btn_change = Button(adminpage, bg = "black", fg = "white", text = "Könyv változtatása")
    btn_change.grid(row = 1, column = 0)

    btn_add = Button(adminpage, bg = "black", fg = "white", text = "Könyv hozzáadása", width = 30)
    btn_add.grid(row = 2, column = 1)


    #def agreement_changed():
    #    print("A válasz", agreement.get())



    #ttk.Checkbutton(adminpage,
                    #text='I agree',
                    #command=agreement_changed,
                    #variable=agreement,
                    #onvalue='agree', state = DISABLED,
                    #offvalue='disagree').grid(row = 3, column = 1)
    
    sor = 3

    for i in range(len(booksList)):
        if(actual.rented == True):
            ttk.Checkbutton(adminpage, text=str(i+1) + ". " + actual.writer + ": " + actual.title, state = DISABLED).grid(row = sor, column = 1)
        else:
            ttk.Checkbutton(adminpage, text=str(i+1) + ". " + actual.writer + ": " + actual.title, command = bookRent(i+1)).grid(row = sor, column = 1)

        #TitleLabel = Label(adminpage, text=str(i+1) + ". " + actual.writer + ": " + actual.title)
        
        #TitleLabel.grid(row = sor, column = 1)
        sor += 1


    adminpage.mainloop()

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


btn_login = Button(root, text="Bejelentkezés", bg = "black", fg = "white", command=lambda:login()).grid(row = 5, column = 1)

root.mainloop()