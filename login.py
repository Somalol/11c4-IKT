from tkinter import *


root = Tk()
root.title("Bejelentkezés")
root.configure(bg = "black")

lista = []

lbl_felh = Label(root, text = "Felhasználónév:", bg="black", fg="white")
lbl_felh.grid(row = 1, column = 0)
etr_fhszn = Entry(root, bg = "lightblue")
etr_fhszn.grid(row = 1, column = 1)

lbl_jelszo = Label(root, text = "Jelszó: ", bg = "black", fg = "white")
lbl_jelszo.grid(row = 2, column = 0)
etr_jelszo = Entry(root, bg = "lightblue")
etr_jelszo.grid(row = 2, column = 1)


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

    print(benev, befhsz, bejelszo, betype)

btn_login = Button(root, text="Bejelentkezés", bg = "black", fg = "white", command=lambda:login()).grid(row = 3, column = 1)

root.mainloop()