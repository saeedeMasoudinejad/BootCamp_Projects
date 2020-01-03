from datetime import*
from dateutil.relativedelta import*
from Mapsa_libery_auto import lib_db
from datetime import *
import json


class admin_member:
    def __init__(self, name, age, id, trustee, level):
        self.name = name
        self.id_mem = id
        self.age = age
        self.time_join = datetime.now()
        self.books_rent = []
        self.trustee = trustee
        self.current_book_rent = []
        self.penalty = 0
        # self.add = self.adduser()
        self.level = level
        self.db = lib_db.DataBase('db_lib')


    # def extend(self):
    #     self.time_join += relativedelta(years=1)

    # def expirecheck(self):
    #     expire_status = False
    #     expire_time = self.time_join
    #     expire_time = expire_time + relativedelta(years=1)
    #     if expire_time <= datetime.now():
    #         expire_status = True
    #     return expire_status

    def add_user(self, username, password, name, age,level):

        re = self.db.cursor.execute("select id from user where username = '{}'".format(username)).fetchall()
        if re == []:
            self.db.cursor.execute("insert into user(username, password, name, age, trustee, level) values"
                              "('{}', '{}', '{}', {}, 0, {})".format(username, password, name, age, level))
            self.db.connection.commit()
            print("This user is register")
        else:
            print("This username is exist")
        # try:
        #     with open("member.json") as outfile:
        #         pass
        # except IOError:
        #     list_member = {"mem": []}
        #     with open("member.json", 'w') as outfile:
        #         json.dump(list_member, outfile)
        # with open('member.json') as outfile:
        #     list_member = json.load(outfile)
        # list_member["mem"].append({"id": self.id_mem,"name": self.name, "age": self.age,"time_join": str(self.time_join),
        #                            "book_rent": self.books_rent, "trustee": self.trustee,
        #                            "current_rent": self.current_book_rent, "penalty": self.penalty})
        # with open('member.json', 'w') as outfile:
        #     json.dump(list_member, outfile)
        # return

    def add_ex_book(self, b_name, b_author, b_isbn, b_category, b_type, b_lang, b_translator ):
        self.db.cursor.execute("insert into book (name, author, ISBN, category, status, type, language, translator) "
                               "values ('{}', '{}', {}, '{}', {}, {}, '{}', '{}')".format(b_name, b_author, b_isbn,
                                                                                    b_category, 1, b_type, b_lang,
                                                                                    b_translator))
        self.db.connection.commit()

    def add_in_book(self, b_name, b_author, b_isbn, b_category, b_type, b_lang):
        self.db.cursor.execute("insert into book (name, author, ISBN, category, status, type, language) "
                               "values ('{}', '{}', {}, '{}', {}, {}, '{}')".format(b_name, b_author, b_isbn,
                                                                                    b_category, 1, b_type, b_lang))
        self.db.connection.commit()

    def rentbook(self, username, book_name):
        search_exist_book = self.db.cursor.execute("select count(id) from book where name = '{}' and status = 1".format(book_name)).fetchall()
        if search_exist_book[0][0] == 0:
            return "This book is not available"
        else:
            block_sitution = self.db.cursor.execute("select bolck from user where username = '{}'".
                                                    format(username)).fetchall()
            if block_sitution[0][0] == 0:
                id_mem = self.db.cursor.execute("select id from user where username = '{}'".format(username)).fetchall()
                id_book = self.db.cursor.execute("select id from book where name = '{}' and status = 1".format(book_name))\
                .fetchall()
                self.db.cursor.execute("insert into rent (book_id, member_id, return_status) values ({},{},0)".format(
                id_book[0][0], id_mem[0][0]))
                self.db.cursor.execute("update book set status = 0 where id = {}".format(id_book[0][0]))
                self.db.connection.commit()
                return 'Book is rented to member.'
            elif block_sitution[0][0] == 1:
                return "'{}' can't rent any book".format(username)

    def extend_deadline(self, username, book_id):
        id_mem = self.db.cursor.execute("select id from user where username = '{}'".format(username)).fetchall()
        # rent_id = self.db.cursor.execute(" select ")
        str_date = self.db.cursor.execute("select start_date_lend from rent where book_id = {} and "
                                          "member_id = {} and return_status = 0"
                                          .format(book_id, id_mem[0][0])).fetchall()
        date_rent = datetime.strptime(str_date[0][0], '%Y-%m-%d %H:%M:%S')
        date_rent += relativedelta(months=1)
        self.db.cursor.execute("update rent set  start_date_lend = '{}' where book_id = {} and member_id = {} and "
                               "return_status = 0".format(date_rent, book_id, id_mem[0][0]))
        self.db.connection.commit()

    def add_remove_black_list(self, info_action):
        action = info_action.split(':')
        if action[0] == 'add':
            self.db.cursor.execute("update user set bolck = 1 where username = '{}'".format(action[1]))
            self.db.connection.commit()
        elif action[0] == 'remove':
            self.db.cursor.execute("update user set bolck = 0 where username = '{}'".format(action[1]))
            self.db.connection.commit()

    def return_book(self, book_id, username):
        user_id = self.db.cursor.execute("select id from user where username = '{}'".format(username)).fetchall()
        self.db.cursor.execute("update rent set return_status = 1 where book_id = '{}' and "
                               "member_id = '{}' and return_status = 0".format(book_id, user_id[0][0]))
        self.db.cursor.execute("update book set status = 1 where id = '{}'".format(book_id))
        self.db.connection.commit()
        return '{} returned the book.'.format(username)

    # def watch_book_list(self):
    #     book_list = []
    #     a = self.db.cursor.execute("select id,name,count(*) from book group by(name)").fetchall()
    #     b = self.db.cursor.execute("select name,count(*) from book where status = 1 group by(name)").fetchall()
    #     exist_flag = 0
    #     for i in a:
    #         for j in b:
    #             if i[1] == j[0]:
    #                 book_list.insert(0, [i[0], i[1], i[2], j[1]])
    #
    #                 exist_flag = 1
    #         if exist_flag == 0:
    #             book_list.insert(0, [i[0], i[1], i[2], 0])
    #     return book_list
    #
    # def watch_list_lend_book(self, yourself_username):
    #     rent_list = self.db.cursor.execute(
    #         "SELECT rent.book_id, book.name,rent.start_date_lend FROM rent JOIN user ON rent.member_id = user.id JOIN book ON rent.book_id = book.id "
    #         "where user.username = '{}'".format(yourself_username)).fetchall()

class usual_member:
    def __init__(self, username, name, age, id, trustee, level):
        self.username = username
        self.name = name
        self.id_mem = id
        self.age = age
        self.time_join = datetime.now()
        self.books_rent = []
        self.trustee = trustee
        self.current_book_rent = []
        self.penalty = 0
        # self.add = self.adduser()
        self.level = level
        self.db = lib_db.DataBase('db_lib')

    def watch_book_list(self):
        book_list = []
        a = self.db.cursor.execute("select id,name,count(*) from book group by(name)").fetchall()
        b = self.db.cursor.execute("select name,count(*) from book where status = 1 group by(name)").fetchall()
        exist_flag = 0
        for i in a:
            for j in b:
                if i[1] == j[0]:
                    book_list.insert(0, [i[0], i[1], i[2], j[1]])

                    exist_flag = 1
            if exist_flag == 0:
                book_list.insert(0, [i[0], i[1], i[2], 0])
        return book_list

    def watch_list_lend_book(self, yourself_username):
        rent_list = self.db.cursor.execute(
            "SELECT rent.book_id, book.name,rent.start_date_lend FROM rent JOIN user ON rent.member_id = user.id JOIN book ON rent.book_id = book.id "
            "where user.username = '{}'".format(yourself_username)).fetchall()
        return rent_list
#u1 = MEMBER("ali", 12)
#u2 = MEMBER("bahram", 22)
#u2 = MEMBER("saeed", 26)
#u2 = MEMBER("sara", 24)
#print(u1.id_mem)

#print(u2.time_join)
#u2.extend()
#u2.expirecheck()
#print(u2.time_join)

