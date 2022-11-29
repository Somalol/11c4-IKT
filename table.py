import tkinter as tk
from tkinter import ttk

def show():

    tempList = [['Jókai Mór','Kőszívű ember fiai', True], ['Molnár Ferenc','A Pál utcai fiúk', False], ['Homérosz', 'Odüsszeia', True], ['Gogol', 'Köpönyeg', False]]
    tempList.sort(key=lambda e: e[1], reverse=True)

    for i, (name, title, borrowed) in enumerate(tempList, start=1):
        listBox.insert("", "end", values=(i, name, title, borrowed))

books = tk.Tk() 
label = tk.Label(books, text="Könyvek", font=("Arial",30)).grid(row=0, columnspan=4)
# create Treeview with 3 columns
cols = ('Position', 'Író', 'Cím', 'Kölcsönzött-e')
listBox = ttk.Treeview(books, columns=cols, show='headings')
# set column headings
for col in cols:
    listBox.heading(col, text=col)    
listBox.grid(row=1, column=0, columnspan=2)

showScores = tk.Button(books, text="Show books", width=15, command=show).grid(row=4, column=0)
closeButton = tk.Button(books, text="Close", width=15, command=exit).grid(row=4, column=1)

books.mainloop()




def show():
        tempList = [booksList]
        tempList.sort(key=lambda e: e[1], reverse=True)

        for i, (title, writer, pages, date , rented) in enumerate(tempList, start=1):
            listBox.insert("", "end", values=(i, title, writer, pages, date , rented))
 
    label = Label(mod, text="Könyvek", font=("Arial",30)).grid(row=0, columnspan=4)
    # create Treeview with 3 columns
    cols = ('Position', 'Cím', 'író', 'oldalak', 'megírt', 'Kölcsönzött-e')
    listBox = ttk.Treeview(mod, columns=cols, show='headings')
    # set column headings
    for col in cols:
        listBox.heading(col, text=col)    
    listBox.grid(row=1, column=0, columnspan=5)

    showScores = Button(mod, text="Show books", width=15, command=show).grid(row=4, column=0)
    closeButton = Button(mod, text="Close", width=15, command=exit).grid(row=4, column=1)
