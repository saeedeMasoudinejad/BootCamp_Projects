from Mapsa_libery_auto import Member
from uuid import*
from dateutil.relativedelta import*
from datetime import *
import json

class Book:
    def __init__(self, name,  author, category, ISBN):
        self.name = name
        self.author = author
        self.ISBN = ISBN
        self.category = category
        self.bookId = uuid4()
        self.status = True
        self.rent = []
        self.current_len = []
        self.add = self.add_book()

    # def rentbook(self, member):
    #     if self.status == False:
    #         print("This book is not availabel")
    #     else:
    #         if Member.MEMBER.expirecheck(member) == False:
    #             if len(member.current_book_rent) < 2:
    #                 member.books_rent.append(self.bookId)
    #                 self.rent.append(member.id_mem)
    #                 self.status = False
    #                 member.trustee = True
    #                 member.current_book_rent.append(self.bookId)
    #                 self.current_len.append((member.id_mem, datetime.now()))
    #             else:
    #                 print("you don't limit borrow more book")
    #         else:
    #             print("your membership is expire")

    def ReturnBook(self, member):
        member.current_book_rent.remove(self.bookId)
        deadline = self.current_len[0][1] + timedelta(days=15)
        if deadline < datetime.now():
            member.penalty += 2000
        self.status = True
        del self.current_len[0]

    def add_book(self):
        try:
            with open("book.json"):
                pass
        except IOError:
            list_book = {"book": []}
            with open("book.json", 'w') as outfile:
                json.dump(list_book, outfile)
        with open('book.json') as outfile:
            list_book = json.load(outfile)
        list_book["book"].append(
            {"id": str(self.bookId), "name": self.name, "author": self.author, "ISBN": self.ISBN, "category": self.category,
             "status": self.status, "rent": self.rent, "curent_rent_person": str(self.current_len)})
        with open('book.json', 'w') as outfile:
            json.dump(list_book, outfile)
        return


class InternalBook(Book):
    def __init__(self, name,  author, category, ISBN):
        super().__init__(name,  author, category, ISBN)
        self.language = "persian"
        self.type = "Internal"

        # def add_book(self):
        #     try:
        #         with open("book.json"):
        #             pass
        #     except IOError:
        #         list_book = {"book": []}
        #         with open("book.json", 'w') as outfile:
        #             json.dump(list_book, outfile)
        #     with open('book.json') as outfile:
        #         list_book = json.load(outfile)
        #     list_book["book"].append(
        #         {"id": str(self.bookId), "name": self.name, "author": self.author, "ISBN": self.ISBN,
        #          "category": self.category,"status": self.status, "rent": self.rent,
        #          "curent_rent_person": str(self.current_len), "language": })
        #     with open('book.json', 'w') as outfile:
        #         json.dump(list_book, outfile)
        #     return

class ExternalBook(Book):
    def __init__(self, name,  author, category, ISBN, language, translator):
        Book.__init__(self, name,  author, category, ISBN)
        self.language = language
        self.translator = translator
        self.type = "External"


#a = InternalBook("پاییز فصل آخر است", "نسیم مرعشی", "رمان", 75676735)
# b = ExternalBook("وقتی نیچه گریست", "اروین یالوم", "رمان", 6543654, "latin", "سپیده حبیب")
# c = Book("CLRS", "Thomas H", "علمی", 43862)
# u1 = Member.MEMBER("ali", 12)
# u1.time_join -= relativedelta(years=10)
#
# print(u1.time_join)
# u2 = Member.MEMBER("bahram", 22)
# u3 = Member.MEMBER("saeed", 26)
# u24= Member.MEMBER("sara", 24)
# a.rentbook(u2)
# b.rentbook(u2)
# print(u2.penalty)
# a.ReturnBook(u2)
# print(a.current_len)
# print(b.current_len)
# print(u2.current_book_rent)
# print(u2.books_rent)
# print(u2.penalty)



