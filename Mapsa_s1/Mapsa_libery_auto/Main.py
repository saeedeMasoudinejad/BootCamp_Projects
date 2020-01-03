from Mapsa_libery_auto import Book, login_lib, lib_db
from Mapsa_libery_auto import Member

import json


class main:
    username = input("please enter your username:")
    password = input("please enter your password:")
    obj_login = login_lib.Login()
    mem = obj_login.check(username, password)
    # print(mem.name,mem.age,mem.id_mem,mem.trustee,mem.level)
    if mem.level == 1:
        action = input("choose your action, if you want add new memeber press 1\n add new book press 2\n "
                       "add a new book is rented by a member press 3\n extend the time of borrow book press 4\n"
                       " add to or remove from black list press 5\n return book press 6\n"
                       "exit from system press 7\n")
        if action == '1':
            new_username = input("please enter the username:")
            new_password = input("please enter the password:")
            new_name = input("please enter the name:")
            new_age = input("please enter the age:")
            new_level = input("please enter 1 if this user is admin and enter 0 if is usal member:")
            mem.add_user(new_username, new_password, new_name, new_age, new_level)
        if action == '2':
            new_book_name = input("please enter the name of the book:")
            new_book_author = input("please enter the writer of the book:")
            new_book_isbn = int(input("please enter the ISBN of book:"))
            new_book_category = input("please determain the category of t book:")
            new_book_type = int(input("please enter 1 if the book in external and 0 if is internal"))
            new_book_lang = input("please enter the language of the book:")
            if new_book_type == 1:
                new_book_tranlator = input("please enter the name of book's translator:")
                mem.add_ex_book(new_book_name, new_book_author, new_book_isbn, new_book_category, new_book_type ,
                                new_book_lang, new_book_tranlator)
            else:
                mem.add_in_book(new_book_name, new_book_author, new_book_isbn, new_book_category, new_book_type,
                                new_book_lang)
        if action == '3':
            rent_book_name = input("please enter the name of book:")
            rent_username = input("please enter the username:")
            mem.rentbook(rent_username, rent_book_name)
            # print("you request is commit")
        if action == '4':
            rent_book_id = input("please enter the id of book:")
            rent_username = input("please enter the username:")
            mem.extend_deadline(rent_username, rent_book_id)
        if action == '5':
            type_action = input("if you want add to black list enter add:username,"
                                "if you want remove to black list enter remove:username")
            mem.add_remove_black_list(type_action)
        if action == '6':
            rent_book_id = input("please enter the id of book:")
            rent_username = input("please enter the username:")
            mem.return_book(rent_book_id, rent_username)
    elif mem.level == 0:
        action = input("choose your action, watch the list of book 1\n watch the lended book 2\n ")
        if action == '1':
            book_list = mem.watch_book_list()
            for h in book_list:
                print(h)
        if action == '2':
            print(mem.watch_list_lend_book(mem.username))
    # continue_flag = False
    # print("if you want do any action,press Y")
    # doning = input()
    # if doning == "Y":
    #     continue_flag = True
    # while continue_flag:
    #     print("if you want add member,please write M. if you want add new book,please write B. if you want determin a renty book"
    #             "please Enter the R")
    #     fun = input()
    #     if fun == "M":
    #         print("please write the name of member")
    #         num_mem = input()
    #         print("please write the age of member")
    #         adge_mem = input()
    #         Member.MEMBER(num_mem, adge_mem)
    #         print("This member added successfully")
    #     elif fun == "B":
    #         print("please write the name of the book")
    #         book_name = input()
    #         print("please write the name of the writer:")
    #         wirter_name = input()
    #         print("please detect the category of the book:")
    #         category_book = input()
    #         print("please write the ISBN of the book:")
    #         isbn_book = input()
    #         Book.Book(book_name, wirter_name, category_book, isbn_book)
    #     elif fun == "R":
    #         print("plese write the id of membership")
    #         mem_id = input()
    #         print("please write the name of the book:")
    #         num_book = input()
    #         with open("book.json") as b:
    #             book_list = json.load(b)
    #         with open("member.json") as m:
    #             mem_list = json.load(m)
    #         for j in mem_list["mem"]:
    #             #print(type(j['id']))
    #             if j['id'] == int(mem_id):
    #                 mem_temp = Member.MEMBER(j["name"], j["age"])
    #         for i in book_list["book"]:
    #             if i["name"] == num_book:
    #                 book_temp = Book.Book(i["name"],i["author"],i["category"],i["ISBN"])
    #                 book_temp.rentbook(mem_temp)
    #                 print("The borrow book is register")
    #     print("if you want do anyting else,press Y otherwise press N")
    #     doagain = input()
    #     if doning == "N":
    #         continue_flag = False