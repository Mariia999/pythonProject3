class Book:
    def __init__(self, genre, title, author):
        self.genre = genre
        self.title = title
        self.author = author

class Reader:
    def __init__(self, fullName, numberOfTicket, dateOfBirth, telefonNumber):
        self.fullName = fullName
        self.numberOfTicket =numberOfTicket
        self.dateOfBirth = dateOfBirth
        self.telefonNumber = telefonNumber

class Library:
    def __init__(self, adress, telefonNumber, book: Book, reader: Reader):
        self.adress = adress
        self.telefonNumber = telefonNumber
        self.book = book
        self.reader = reader


    def takeBook(self=None):
        return f'{self.fullName} vzyav knigu: {self.book}'

    def returnBook(self=None):
        return f'{self.fullName} povernuv knigu: {self.book}'





b1 = Book('poema', 'Eneida', 'Kolyarevskiy')
b2 = Book('poeziya', 'Kobzar', 'Shevchenko')
b3 = Book('poeziya', 'Lisova pisnya', 'Ukrainka')
b4 = Book('poeziya', 'Zacharovana Desna', 'Dovgenko')
b5 = Book('dramaturgiya', 'Kaidasheva Sim`ya', 'Levickiy')