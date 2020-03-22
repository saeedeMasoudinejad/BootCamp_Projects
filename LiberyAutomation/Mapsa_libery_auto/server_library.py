from Mapsa_libery_auto import login_lib, lib_db, Book, Member, log_lib
import select
import socket
import random


class Server:
    def __init__(self, ip, port):
        self.login = login_lib.Login()
        self.login_users = {}
        self.map_username_socket = {}
        self.attempt = {}
        self.enter_numbers = {}
        self.db = lib_db.DataBase('db_lib')
        self.db_mongo = log_lib.Log()
        self.blacklist = []
        self.login_username = []
        self.IP = ip
        self.PORT = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sockets = [self.server_socket]
        self.__setup()

    def __setup(self):
        self.server_socket.bind((self.IP, self.PORT))
        self.server_socket.listen(10)
        print('Library up!')
        self.__run()

    def __run(self):
        while True:
            read_socket, write_socket, exception_socket = select.select(self.sockets, [], self.sockets)
            for sock in read_socket:
                if sock == self.server_socket:
                    self.__connected_to()
                else:
                    try:
                        message = self.__recv_msg(sock)

                        if len(message) > 5:
                            prefix = message[:5]
                            message = message[5:]
                            if prefix == '#user':
                                self.__act_login(message, sock)
                            elif prefix == '#at11':
                                self.__act_add_member(message, sock)
                            elif prefix == '#at12':
                                self.__act_add_book(message, sock)
                            elif prefix == '#at13':
                                self.__act_rent_book(message, sock)
                            elif prefix == '#at14':
                                self.__act_extend_lend(message, sock)
                            elif prefix == '#at15':
                                self.__act_blacklist(message, sock)
                            elif prefix == '#at16':
                                self.__act_return_book(message, sock)
                            elif prefix == '#at02':
                                self.__show_my_books(message, sock)
                            else:
                                print(message)
                        else:
                            if message == '#at01':
                                self.__show_books(sock)
                            elif message == '#at55':
                                self.sockets.remove(sock)
                                del self.login_users[sock]
                                del self.map_username_socket[sock]
                                self.__send_msg(sock, 'You exit. Bye.')
                                self.sockets.remove(sock)
                                del self.attempt[sock]
                                self.login_username.remove(self.map_username_socket[sock])
                    except Exception:
                        continue

    def __connected_to(self):
        client_socket, address = self.server_socket.accept()
        self.sockets.append(client_socket)

    def __send_msg(self, s, msg):
        s.send(bytes(msg, 'utf-8'))

    def __recv_msg(self, s):
        msg = s.recv(1024)
        return msg.decode('utf-8')

    def __act_login(self, msg, s):
        login_data = msg.split('##')
        username = login_data[0]
        password = login_data[1]
        login_user_flag = False
        if username in self.login_username :
                login_user_flag = True
        if login_user_flag == False:
            member = self.login.check(username, password)
            if member:

                self.login_users[s] = member
                self.map_username_socket[s] = username
                print("{} logged in successfully.".format(username))
                self.__send_msg(s, '#OK')
                self.__send_msg(s, str(member.level))
                self.login_username.append(username)
                self.db_mongo.add_log('{}'.format(s), username, 'login', 1)
            else:
                # self.__send_msg(s, '#Failed')
                self.db_mongo.add_log('{}'.format(s), username, 'login', 0)
                if s not in self.attempt:
                    self.attempt[s] = 1
                else:
                    self.attempt[s] += 1
                if self.attempt[s] >= 2:
                    self.__send_msg(s, '#captcha')
                    while True:
                        flag_check = "F"
                        # print('you entered incorrect user name and password too many times')
                        # print('you need to enter captcha to continue using our system')
                        captcha = login_lib.Captcha()
                        self.__send_msg(s, 'Captcha: {}'.format(captcha.code))
                        input_captcha = self.__recv_msg(s)
                        captcha.validation_time()
                        if int(input_captcha) == captcha.code:
                            self.attempt[s] = 2
                            flag_check = "T"
                            self.__send_msg(s, flag_check)
                            break
                        else:
                            self.__send_msg(s, flag_check)
                else:
                    self.__send_msg(s, '#failed')
        else:
            self.__send_msg(s, '#Duplicate')

    def __act_add_member(self, msg, s):
        msg = msg.split('##')
        mem = self.login_users[s]
        mem.add_user(msg[0], msg[1], msg[2], msg[3], msg[4])
        print('admin added {} to members'.format(msg[0]))
        self.__send_msg(s, 'member added')
        self.db_mongo.add_log('{}'.format(s), self.map_username_socket[s], 'member added', 1)

    def __act_add_book(self, msg, s):
        msg = msg.split('##')
        mem = self.login_users[s]
        if msg[4] == '0':
            mem.add_in_book(msg[0], msg[1], msg[2], msg[3], msg[4], msg[5])
        else:
            mem.add_ex_book(msg[0], msg[1], msg[2], msg[3], msg[4], msg[5], msg[6])
        print('admin added {} to books'.format(msg[0]))
        self.__send_msg(s, 'book added')
        self.db_mongo.add_log('{}'.format(s), self.map_username_socket[s], 'book added', 1)

    def __act_extend_lend(self, msg, s):
        msg = msg.split('##')
        user_extend = msg[0]
        book_extend = int(msg[1])
        mem = self.login_users[s]
        mem.extend_deadline(user_extend, book_extend)
        self.__send_msg(s, 'Return date was extended for 30 days.')
        self.db_mongo.add_log('{}'.format(s), self.map_username_socket[s], 'extend_lend_time', 1)

    def __act_blacklist(self, msg, s):
        mem = self.login_users[s]
        mem.add_remove_black_list(msg)
        self.__send_msg(s, 'It is done')
        self.db_mongo.add_log('{}'.format(s), self.map_username_socket[s], 'add_remove_black_list', 1)

    def __show_books(self, s):
        mem = self.login_users[s]
        books_list = mem.watch_book_list()
        books = ''
        for book in books_list:
            books += '{}'.format(book[0]) + '*' + '{}'.format( book[1] )+ '*' + str(book[2]) + '*' + str(book[3]) + '##'
        self.__send_msg(s, books[:-2])
        self.db_mongo.add_log('{}'.format(s), self.map_username_socket[s], 'watch_book_list', 1)

    def __show_my_books(self, msg, s):
        mem = self.login_users[s]
        my_books_list = mem.watch_list_lend_book(msg)
        books = ''
        for book in my_books_list:
            books += (str(book[0]) + '*' + '{}'.format(book[1]) + '*' + '{}'.format(book[2]) + '##')
        self.__send_msg(s, books[:-2])
        self.db_mongo.add_log('{}'.format(s), self.map_username_socket[s], 'watch_yourself_book_list', 1)

    def __act_rent_book(self, msg, s):
        msg = msg.split('##')
        rent_book_name = msg[0]
        rent_user_name = msg[1]
        mem = self.login_users[s]
        result = mem.rentbook(rent_user_name, rent_book_name)
        self.__send_msg(s, result)
        self.db_mongo.add_log('{}'.format(s), self.map_username_socket[s], 'rent_new_book', 1)

    def __act_return_book(self, msg, s):
        msg = msg.split('##')
        return_book_id = int(msg[0])
        return_book_member = msg[1]
        mem = self.login_users[s]
        result = mem.return_book(return_book_id, return_book_member)
        self.__send_msg(s, result)
        self.db_mongo.add_log('{}'.format(s), self.map_username_socket[s], 'return_a_boo_rented', 1)

Server('192.168.1.7', 2302)
