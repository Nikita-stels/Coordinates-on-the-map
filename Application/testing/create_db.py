import sys
sys.path[0] = sys.path[0][:-8]
from scripts.logic.utilities import ConnectDB


class CreateDB():
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


a = CreateDB()
print(a.create_tabl())
print(a.create_index())
print(a.insert_test_coordinate())


# centr_test = (48.704578, 44.507112)
# in_circle = """
#                 Select id, Lat, Lon,
#                     acos(sin(radians(48.704578))*sin(radians(Lat)) + cos(radians(48.704578))*cos(radians(Lat))*cos(radians(Lon)-radians(44.507112))) * 6371 As D
#                 From coordinate
#                 Where acos(sin(radians(48.704578))*sin(radians(Lat)) + cos(radians(48.704578))*cos(radians(Lat))*cos(radians(Lon)-radians(44.507112))) * 6371 < 5;
#                 """