import os
import json
import psycopg2
# from bson.objectid import ObjectId
# OS = sys.platform


class ConnectDB():
    """Class for connect to DB."""
    def __init__(self):
        self.conn = psycopg2.connect(**self.config_app()['Data_Base'])
        self.cursor = self.conn.cursor()

    def config_app(self):
        path = os.getcwd() + "\Application\config.json" ######### !!!\config.json
        with open(path) as config:
            json_str = config.read()
            return json.loads(json_str)

    def close(self):
        self.conn.close()
        self.cursor.close()


class WrapperDB:
    """Class for requests DB."""
    #self.connect_db.conn.commit()
    def __init__(self):
        self.connect_db = ConnectDB()

    def get_all_coordinate(self) -> list:
        """  """
        request = """ SELECT * FROM coordinate """
        self.connect_db.cursor.execute(request)
        return self.connect_db.cursor.fetchall()
    
    def __str__(self):
        return __class__.__name__
    
    


class Destributor:
    def __init__(self):
        pass
