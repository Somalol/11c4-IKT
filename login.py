from tkinter import *
import bookDisplay 

booksList = []

root = Tk()
root.title("Bejelentkezés")
root.geometry("170x170")

lista = []
booksList = []

lbl_felh = Label(root, text = "Felhasználónév:")
lbl_felh.grid(row = 0, column = 1, padx = 20)
etr_fhszn = Entry(root, width = 20)
etr_fhszn.grid(row = 1, column = 1, padx = 20, pady = 5)

lbl_jelszo = Label(root, text = "Jelszó: ")
lbl_jelszo.grid(row = 2, column = 1, padx = 20)
etr_jelszo = Entry(root, width = 20,  show="*")
etr_jelszo.grid(row = 3, column = 1, padx = 20, pady = 5)

btn_login = Button(root, text="Bejelentkezés", command=lambda:login()).grid(row = 4, column = 1, pady = 5)
closeBtn = Button(root, text="Bezárás", command=quit ).grid(row=5, column=1)


with open("loginusers.txt", "r", encoding = "utf-8") as adatok:
    for i in adatok:
        sor = i.strip().split(";")
        lista.append({
            "nev" : str(sor[0]),
            "fhsznev" : str(sor[1]),
            "jelszo" : str(sor[2]),
            "rang" : str(sor[3])
        })

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
                root.destroy()
                bookDisplay.adminPage()
            elif(i["rang"] == "user"):
                root.destroy()
                bookDisplay.userPage()

root.mainloop()