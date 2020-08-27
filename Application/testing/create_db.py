import sys
import random
sys.path[0] = sys.path[0][:-8]
from scripts.logic.utilities import ConnectDB


class CreateDB():
    """The class is needed to create a 
    database nugget.

    """
    def __init__(self):
        self.connect_db = ConnectDB()

    def create_tabl(self):
        """Create table coordinate."""
        request = """CREATE TABLE IF NOT EXISTS coordinate(
                            Id serial primary key,
                            Lat DECIMAL(9,6),
                            Lon DECIMAL(9,6)
                    )"""
        self.connect_db.cursor.execute(request)
        self.connect_db.conn.commit()
        return self.connect_db.cursor.statusmessage

    def create_index(self):
        """Create table coordinate."""
        request = "CREATE INDEX indeLat ON coordinate (Lat)"
        self.connect_db.cursor.execute(request)
        self.connect_db.conn.commit()

        request = "CREATE INDEX indeLat ON coordinate (Lon)"
        self.connect_db.cursor.execute(request)
        self.connect_db.conn.commit()
        return self.connect_db.cursor.statusmessage

    def insert_test_coordinate(self):
        """Insert test coordinate."""
        request = """INSERT INTO coordinate (Lat, Lon) VALUES(48.685444, 44.474254), 
                                                                (48.716087, 44.482757), 
                                                                (48.746087, 44.697221); """
        self.connect_db.cursor.execute(request)
        self.connect_db.conn.commit()
        return self.connect_db.cursor.statusmessage
    
    def drop_table(self):
        """Removing all records in a table."""
        request = """DROP TABLE IF EXISTS coordinate"""
        self.connect_db.cursor.execute(request)
        self.connect_db.conn.commit()
        return self.connect_db.cursor.statusmessage

    def generate_big_data(self, quantity):
        """Filling the database with random coordinates."""
        for _ in range(quantity):
            latitude = round(random.random() * 89, 6)
            longitude = round(random.random() * 179, 6)
            request = f"""INSERT INTO coordinate (Lat, Lon) VALUES({latitude}, {longitude})"""
            self.connect_db.cursor.execute(request)
            self.connect_db.conn.commit()
        return self.connect_db.cursor.statusmessage
        

def create_db():
    db = CreateDB()
    db.drop_table()
    db.create_tabl()
    db.create_index()
    status = db.insert_test_coordinate()
    if status == "INSERT 0 3":
        print("ok")
    else:
        print("Error")

# create_db()

def create_big_data():
    db = CreateDB()
    db.drop_table()
    db.create_tabl()
    
    db.generate_big_data(100000)
    db.create_index()

create_big_data()
