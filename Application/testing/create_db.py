import sys
sys.path[0] = sys.path[0][:-8]
from scripts.logic.utilities import ConnectDB


def creat_db():
    db = ConnectDB().db
    coll_message = db['message']
    coll_users = db['users']

creat_db()


48.704578, 44.507112
create_table_cargo = """CREATE TABLE coordinate(
                            Id serial primary key,
                            Lat DECIMAL(9,6),
                            Lon DECIMAL(9,6)
                    );"""

create_INDEX = """CREATE INDEX index_name ON coordinate (Lat, Lon);
                """

insert_test_coor = """ INSERT INTO coordinate (Lat, Lon) VALUES(48.685444, 44.474254), 
                                                     (48.716087, 44.482757), 
                                                     (48.746087, 44.697221); """



in_circle = """
Select id, Lat, Lon,
       acos(sin(radians(48.704578))*sin(radians(Lat)) + cos(radians(48.704578))*cos(radians(Lat))*cos(radians(Lon)-radians(44.507112))) * 6371 As D
From coordinate
Where acos(sin(radians(48.704578))*sin(radians(Lat)) + cos(radians(48.704578))*cos(radians(Lat))*cos(radians(Lon)-radians(44.507112))) * 6371 < 5;
"""