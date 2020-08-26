import sys
sys.path[0] = sys.path[0][:-8]
from scripts.logic.utilities import ConnectDB


class CreateDB():
    """
    The class is needed to create a database nugget
    """
    def __init__(self):
        self.connect_db = ConnectDB()

    def create_tabl(self):
        """ create table coordinate """
        request = """CREATE TABLE coordinate(
                            Id serial primary key,
                            Lat DECIMAL(9,6),
                            Lon DECIMAL(9,6)
                    )"""
        self.connect_db.cursor.execute(request)
        self.connect_db.conn.commit()
        return self.connect_db.cursor.statusmessage

    def create_index(self):
        """ create table coordinate """
        request = "CREATE INDEX index_name ON coordinate (Lat, Lon)"
        self.connect_db.cursor.execute(request)
        self.connect_db.conn.commit()
        return self.connect_db.cursor.statusmessage

    def insert_test_coordinate(self):
        """ insert test coordinate """
        request = """ INSERT INTO coordinate (Lat, Lon) VALUES(48.685444, 44.474254), 
                                                     (48.716087, 44.482757), 
                                                     (48.746087, 44.697221); """
        self.connect_db.cursor.execute(request)
        self.connect_db.conn.commit()
        return self.connect_db.cursor.statusmessage


def create_db():
    db = CreateDB()
    db.create_tabl()
    db.create_index()
    db.insert_test_coordinate()
    print("ok")

create_db()
