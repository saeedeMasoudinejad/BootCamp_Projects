import pymongo


class Log:
    __instance = 0

    def __init__(self):
        self.myclient = pymongo.MongoClient('mongodb://localhost:27017/')
        self.mydb = self.myclient["Lib_Log"]
        self.mycoll = self.mydb['Log']

    def __new__(cls):
        if Log.__instance == 0:
            Log.__instance = super().__new__(cls)
        return Log.__instance

    def add_log(self, socket, username, action, status):
        if action == 'login':
            level_log = 1
        else:
            level_log = 0
        str_log = {'socket':socket, 'username': username, 'action': action, 'status': status, 'level_log': level_log}
        self.mycoll.insert_one(str_log)

# l = Log()
# l.add_log(124,5346,6557,54654)
# while True:
#     print('test')