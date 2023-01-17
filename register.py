from tkinter import *
import bookDisplay
from tkinter import messagebox

def register(root):
    global befhsz
    global bejelszo
    global benev
    global betype

    if etr_jelszo2.get() != etr_jelszo.get():
        messagebox.showerror(title="Error" ,message="A két jelszó nem egyezik")
    else:
        benev = etr_nev.get()
        befhsz = etr_fhszn.get()
        bejelszo = etr_jelszo.get()
        betype = "user"
        
        with open("loginusers.txt", "a", encoding = "utf-8") as adatok:
            adatok.write("\n" + benev + ";" + befhsz + ";" + bejelszo + ";" + betype)
            root.destroy()

def registerWindow():
    global etr_fhszn
    global etr_jelszo
    global etr_jelszo2
    global etr_nev

    root = Toplevel()
    root.title("Bejelentkezés")
    root.geometry("170x270")

    lbl_nev = Label(root, text = "Név:")
    lbl_nev.grid(row = 0, column = 1, padx = 20)
    etr_nev = Entry(root, width = 20)
    etr_nev.grid(row = 1, column = 1, padx = 20, pady = 5)

    lbl_felh = Label(root, text = "Felhasználónév:")
    lbl_felh.grid(row = 2, column = 1, padx = 20)
    etr_fhszn = Entry(root, width = 20)
    etr_fhszn.grid(row = 3, column = 1, padx = 20, pady = 5)

    lbl_jelszo = Label(root, text = "Jelszó: ")
    lbl_jelszo.grid(row = 4, column = 1, padx = 20)
    etr_jelszo = Entry(root, width = 20,  show="*")
    etr_jelszo.grid(row = 5, column = 1, padx = 20, pady = 5)

    lbl_jelszo2 = Label(root, text = "Jelszó mégegyszer: ")
    lbl_jelszo2.grid(row = 6, column = 1, padx = 20)
    etr_jelszo2 = Entry(root, width = 20,  show="*")
    etr_jelszo2.grid(row = 7, column = 1, padx = 20, pady = 5)

    btn_login = Button(root, text="Regisztrálás", command=lambda:register(root)).grid(row = 8, column = 1, pady = 5)
    closeBtn = Button(root, text="Bezárás", command=quit ).grid(row=9, column=1)

    root.mainloop()


