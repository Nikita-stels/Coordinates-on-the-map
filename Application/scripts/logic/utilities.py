import pymongo
import os
import json
import sys
import time
from bson.objectid import ObjectId
OS = sys.platform


class ConnectDB():
    def __init__(self):
        self.info_db = self.get_info_db()
        self.conn = pymongo.MongoClient(*self.info_db)
        self.db = self.conn.mydb

    def config_app(self):
        path = os.getcwd() + "/Application-VT/config.json"
        with open(path) as config:
            json_str = config.read()
            return json.loads(json_str)

    def get_info_db(self):
        info_db = self.config_app()['Data_Base']
        host, port = info_db['host'], info_db['port']
        return host, int(port)



class WrapperDB:
    def __init__(self):
        self.db = ConnectDB().db
        self.coll_users = self.db.users
        self.coll_message = self.db.message
    

class Destributor:
    def __init__(self):
        pass
