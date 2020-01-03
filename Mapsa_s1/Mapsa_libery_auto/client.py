from Mapsa_libery_auto import Book, login_lib, lib_db
from Mapsa_libery_auto import Member

import select
import socket
import datetime


class Main:
    IP = 'localhost'
    PORT = 2302
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((IP, PORT))
    while True:
        username = input("please enter your username:")
        password = input("please enter your password:")
        client_socket.send(bytes('#user' + username + '##' + password, 'utf-8'))
        # login (successful or failed)
        msg = client_socket.recv(1024).decode('utf-8')
        if msg == '#OK':
            print('{} logged in successfully.'.format(username))
            level = int(client_socket.recv(1024).decode('utf-8'))
            break
        elif msg == '#failed':
            print('Username or password incorrect!')
            continue
        else:
            while True:
                captcha = client_socket.recv(1024).decode('utf-8')
                print(captcha)
                cap = input("Enter this captcha to verify: ")
                client_socket.send(bytes(cap, 'utf-8'))
                flag_check = client_socket.recv(1024).decode('utf-8')
                if flag_check == 'T':
                    break


    # obj_login = login_lib.Login()
    # mem = obj_login.check(username, password)
    # print(mem.name,mem.age,mem.id_mem,mem.trustee,mem.level)
    while True:
        if level == 1:
            action = input("choose your action, if you want add new member press 1\n add new book press 2\n "
                           "add a new book is rented by a member press 3\n extend the time of borrow book press 4\n"
                           " add to or remove from black list press 5\n return book press 6\n"
                           "exit from system press 7\n")
            if action == '1':
                new_username = input("please enter the username:")
                new_password = input("please enter the password:")
                new_name = input("please enter the name:")
                new_age = input("please enter the age:")
                new_level = input("please enter 1 if this user is admin and enter 0 if is usual member:")
                new_user = new_username + '##' + new_password + '##' + new_name + '##' + new_age + '##' + new_level
                client_socket.send(bytes('#at11' + new_user, 'utf-8'))
                print(client_socket.recv(1024).decode('utf-8'))
            elif action == '2':
                new_book_name = input("Enter book name: ")
                new_author = input("Enter book author: ")
                new_isbn = input("Enter book ISBN: ")
                new_category = input("Enter book category: ")
                new_type = input("Enter 0 if this book is internal. Enter 1 if this book is external: ")
                if new_type == '1':
                    new_language = input("Enter book language: ")
                    new_translator = input("Enter book translator: ")
                else:
                    new_language = 'persian'
                    new_translator = ''
                new_book = new_book_name + '##' + new_author + '##' + new_isbn + '##' + new_category + '##' + new_type + '##' + new_language + '##' + new_translator
                client_socket.send(bytes('#at12' + new_book, 'utf-8'))
                print(client_socket.recv(1024).decode('utf-8'))
            elif action == '3':
                rent_book_name = input("please enter the name of book:")
                rent_username = input("please enter the username:")
                client_socket.send(bytes('#at13' + rent_book_name + '##' + rent_username, 'utf-8'))
                print(client_socket.recv(1024).decode('utf-8'))
            elif action == '4':
                extend_user_name = input("Enter username: ")
                extend_book_id = input("Enter book id: ")
                client_socket.send(bytes('#at14' + extend_user_name + '##' + str(extend_book_id), 'utf-8'))
                msg = client_socket.recv(1024).decode('utf-8')
                print(msg)
            elif action == '5':
                type_action = input("if you want add to black list enter 1,"
                                    "if you want remove to black list enter 2")
                user_name_black = input("Enter username: ")
                if type_action == '1':
                    mess = 'add:' + user_name_black
                elif type_action == '2':
                    mess = 'remove:' + user_name_black
                else:
                    print('Your input war incorrect. Please try again!')
                client_socket.send(bytes('#at15' + mess, 'utf-8'))
                msg = client_socket.recv(1024).decode('utf-8')
                if type_action == '1':
                    print('{} is added to blacklist.'.format(user_name_black))
                elif type_action == '2':
                    print('{} is removed from blacklist.'.format(user_name_black))
            elif action == '6':
                return_book_id = input("Enter book id: ")
                return_user_name = input("Enter member username: ")
                client_socket.send(bytes('#at16' + str(return_book_id) + '##' + return_user_name, 'utf-8'))
                print(client_socket.recv(1024).decode('utf-8'))
            elif action == '7':
                client_socket.send(bytes('#at55', 'utf-8'))
                print(client_socket.recv(1024).decode('utf-8'))
                break
            else:
                print("Your input was incorrect. Please try again.")
        else:
            action = input("choose your action, watch the list of book 1\n watch the lend book 2\n "
                           "exit 3\n")
            if action == '1':
                client_socket.send(bytes('#at01', 'utf-8'))
                books_list = client_socket.recv(1024).decode('utf-8')
                books_list = books_list.split('##')
                print('Book ID **** Book Name **** Number of books **** Number of rented')
                print('=====================================================')
                for book_list in books_list:
                    book_list = book_list.split('*')
                    print(book_list[0] + '    ' + book_list[1] + '    ' + book_list[2] + '    ' + book_list[3])
                print('=====================================================')
            elif action == '2':
                client_socket.send(bytes('#at02' + username, 'utf-8'))
                books = client_socket.recv(1024).decode('utf-8').split('##')
                print('Here is the list of your books')
                print('Book ID **** Book Name **** Time')
                print('================================')
                for book in books:
                    book = book.split('*')
                    print(book[0] + '   ' + book[1] + '   ' + book[2])
                print('================================')
            elif action == '3':
                client_socket.send(bytes('#at55', 'utf-8'))
                print(client_socket.recv(1024).decode('utf-8'))
                break
            else:
                print("Your input was incorrect. Please try again.")
