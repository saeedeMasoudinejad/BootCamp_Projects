from Mapsa_libery_auto import lib_db, Member
import random
import time


class Captcha():
    def __init__(self):
        self.code = random.randint(10000, 99999)
        self.created = time.time()
        self.expires_time = 60

    def validation_time(self):
        t = time.time()
        print(t - self.created)
        if t - self.created > self.expires_time:
            print('Captcha is expired')
            self.created += self.expires_time
            self.code = random.randint(10000, 99999)
        return self.code


class Login:
    attempts = 0

    def __init__(self):
        self.db = lib_db.DataBase('db_lib')
        self.__member = None

    def check(self, username, password):
        result = self.db.cursor.execute("select * from user where username = '{}' and password = '{}'".format(
            username, password)).fetchall()
        if result != []:
            # print(result[7])
            if result[0][6] == 0:
                self.__member = Member.usual_member(result[0][1], result[0][3], result[0][4], result[0][0], result[0][5],
                                                    result[0][6])
            else:
                self.__member = Member.admin_member(result[0][3], result[0][4], result[0][0], result[0][5], result[0][6])
            print("{} loing sucssfuly".format(result[0][3]))
            Login.attempts = 0
        # elif Login.attempts >= 2:
        #     while True:
        #         print('you entered incorrect user name and password too many times')
        #         print('you need to enter captcha to continue using our system')
        #         captcha = Captcha()
        #
        #         print('Captcha: {}'.format(captcha.code))
        #         input_captcha = input('Please enter the captcha above: ')
        #         captcha.validation_time()
        #
        #         if int(input_captcha) == captcha.code:
        #             Login.attempts = 2
        #             break
        else:
            self.__member = None
            print("your username or password incorrect!")
            Login.attempts += 1
            print(Login.attempts)

        return self.__member

# test = Login()
# test.check('admin', '123')
