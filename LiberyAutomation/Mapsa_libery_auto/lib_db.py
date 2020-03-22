import sqlite3
import datetime
from dateutil.relativedelta import*

class DataBase:
    __instance = 0

    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        # self.name = 'sara'

    def __new__(cls, db_name):
        if DataBase.__instance == 0:
            DataBase.__instance = super().__new__(cls)
        return DataBase.__instance

# db = DataBase('db_lib')
# print(db.cursor.execute("select * from user").fetchall())
# name = 'sara'
# print(db.cursor.execute("SELECT rent.book_id, book.name,user.username FROM rent JOIN user ON rent.member_id = user.id JOIN book ON rent.book_id = book.id "
#                         "where user.username = '{}'".format(name)).fetchall())
# db.cursor.execute("delete from rent where id = 2")
# db.connection.commit()

# db.cursor.execute("create table user (id integer primary key autoincrement,username varchar(256), "
#                   "password varchar(256),name varchar(256),age int, trustee boolean,level boolean)")
# db.cursor.execute("insert into user(username, password, name, age, trustee, level) values"
#                   "('admin','1234','saeede',26, 0, 1)")

# db.cursor.execute("create table book (id integer primary key autoincrement, name varchar(256), author  varchar(256),"
#                   "ISBN int, category varchar(256), status boolean, type boolean, language varchar(256), "
#                   "translator varchar(256))")
# db.cursor.execute("insert into book (name, author, ISBN, category, status, type, language) values "
#                    "('paiz fasl akhar ast', 'Nasim marashi', 342087, 'novel', 1, 0, 'fa' ) ")
# db.cursor.execute("create table rent (id integer primary key autoincrement ,book_id int, member_id int,"
#                   "start_date_lend TIMESTAMP DEFAULT CURRENT_TIMESTAMP,"
#                   "return_status boolean ,"
#                   "FOREIGN KEY (book_id)REFERENCES book (id)"
#                   ",FOREIGN KEY (member_id)REFERENCES user (id))")
#
# db.cursor.execute("insert into rent (book_id, member_id, return_status) values (3,2,0)")

# print(a[0][3])
# a = db.cursor.execute("select start_date_lend from rent where id = 1 ").fetchall()
# f = datetime.datetime.strptime(a[0][0], '%Y-%m-%d %H:%M:%S')
# print(f)
# f += relativedelta(months= 1)
# print(f)
# print(db.cursor.execute("update rent set  start_date_lend = '{}' where id = 1 ".format(f)).fetchall())
bn = 'CLRS'
# a =db.cursor.execute("select count(id) from book where name = '{}'".format(bn)).fetchall()
# r = db.cursor.execute("select count(id) from book where name = '{}' and status = 1".format(bn)).fetchall()
# print(r[0][0])
# print(a)
# db.cursor.execute("drop table rent")
# name = 'sara'
# print(db.cursor.execute("select * from rent").fetchall())
# db.cursor.execute("insert into rent (book_id, member_id, return_status) values ({},{},0)".format(
#                 id_book, id_mem))
# print(db.cursor.execute("select * from rent ").fetchall())
# db.cursor.execute("alter table user add bolck boolean default 0")
# db.connection.commit()
# print(db.cursor.execute("select * from user").fetchall())
# a = db.cursor.execute("select name,count(*) from book group by(name)").fetchall()
# b = db.cursor.execute("select name,count(*) from book where status = 1 group by(name)").fetchall()
# exist_flag = 0
# for i in a:
#     for j in b:
#         if i[0] == j[0]:
#             print("'{}','{}','{}'".format(i[0],i[1],j[1]))
#             exist_flag = 1
#     if exist_flag == 0:
#         print("'{}','{}',0".format(i[0], i[1]))

# db.connection.commit()