from tkinter import *
import bookDisplay 


booksList = []

root = Tk()
root.title("Bejelentkezés")
root.configure(bg = "black")

lista = []
booksList = []

lbl_felh = Label(root, text = "Felhasználónév:", bg="black", fg="white")
lbl_felh.grid(row = 0, column = 1)
etr_fhszn = Entry(root, bg = "lightblue", width = 30)
etr_fhszn.grid(row = 1, column = 1)

lbl_jelszo = Label(root, text = "Jelszó: ", bg = "black", fg = "white")
lbl_jelszo.grid(row = 2, column = 1)
etr_jelszo = Entry(root, bg = "lightblue", width = 30)
etr_jelszo.grid(row = 3, column = 1)

lbl_uj = Label(root, text = "Még nem regisztrált? Tegye meg!", bg = "black", fg = "white")
lbl_uj.grid(row = 5, column = 1)
btn_regist = Button(root, text = "Regisztrálok", bg = "black", fg = "white", command = lambda:regist()).grid(row = 6, column = 1)


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

def regist():
    reg = Tk()
    reg.title("Regisztráció")
    reg.configure(bg = "black")

    lbl_nev = Label(reg, text="Teljes neve:", bg = "black", fg = "white")
    lbl_nev.grid(row = 0, column = 1)
    etr_nev = Entry(reg, bg = "lightblue", width = 30)
    etr_nev.grid(row = 1, column = 1)

    lbl_felh1 = Label(reg, text = "Felhasználónév:", bg="black", fg="white")
    lbl_felh1.grid(row = 2, column = 1)
    etr_fhszn1 = Entry(reg, bg = "lightblue", width = 30)
    etr_fhszn1.grid(row = 3, column = 1)

    lbl_jelszo1 = Label(reg, text = "Jelszó: ", bg = "black", fg = "white")
    lbl_jelszo1.grid(row = 4, column = 1)
    etr_jelszo1 = Entry(reg, bg = "lightblue", width = 30)
    etr_jelszo1.grid(row = 5, column = 1)

    btn_regist1 = Button(reg, text = "Regisztrálok!", bg = "black", fg = "white", command = lambda:bumm())
    btn_regist1.grid(row = 6, column = 1)

    def bumm():
        with open("loginusers.txt", "a", encoding = "utf-8") as adatok:
            adatok.writelines("\n" + etr_nev.get() + ";" + etr_fhszn1.get() + ";" + etr_jelszo1.get() + ";" + "user")


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
                bookDisplay.adminPage()
            #elif(i["rang"] == "user"):
            #   bookDisplay.userPage()


btn_login = Button(root, text="Bejelentkezés", bg = "black", fg = "white", command=lambda:login()).grid(row = 4, column = 1)

root.mainloop()