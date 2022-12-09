from bookClass import Book

booksList = []
def fileRead():
        booksList.clear()
        with open("books.txt", 'r', encoding = 'utf-8') as f:
            for line in f:
                title, publisher, writer, pages,date, rented = line.strip().split(";")
                actual = Book(title.strip(), publisher.strip(), writer.strip(), pages.strip(), date.strip(), rented.strip())
                booksList.append(actual)
        return booksList
