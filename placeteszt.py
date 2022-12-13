from tkinter import *

root = Tk()
root.title("szia")

label1 = Label(text = "Ez az alalp szöveg")
label1.place(x = 20, y = 20)

label2 = Label(text = "Ez tőle jobbra van")
label2.place(relx= 0.8, relwidth= 0.5, anchor="w")

root.mainloop()