
class Book:

    def __init__(self, Title, Author, Price):
        self.Title = Title
        self.Author = Author
        self.Price = Price


    def view(self):
        return ("Book Title: ", self.Title, "Book Author: ", self.Author, "Book Price: ", self.Price)


MyBook = Book("Python Crash Course", "Eric Matthes", "23 $")
print(MyBook.view())