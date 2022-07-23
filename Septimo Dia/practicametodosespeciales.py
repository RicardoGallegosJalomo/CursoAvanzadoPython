# Practice de Methods Specials

class Book:

    def __init__(self, title, author, amount_pages):

        self.title = title
        self.author = author
        self.amount_pages = amount_pages

    def __str__(self):
        
        return f'"{self.title}", de {self.author}'


book1 = Book('Bronco','Lupe',25)

print(book1)

