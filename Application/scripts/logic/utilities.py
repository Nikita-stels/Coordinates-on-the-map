import os
import json
import psycopg2


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

    def get_users_coordinate(self, center_lat, center_lon, radius) -> list:
        """ 
        returns a sheet with coordinates 
        included in the desired radius
        center_lat, center_lon - latitude and longitude in radians
        radius - in kilometers
        """
        request = f"""
                Select id, Lat, Lon
                From coordinate
                Where acos(sin(radians({center_lat}))*sin(radians(Lat)) + cos(radians({center_lat}))*cos(radians(Lat))*cos(radians(Lon)-radians({center_lon}))) * 6371 < {radius}
                """
        self.connect_db.cursor.execute(request)
        return self.connect_db.cursor.fetchall()

    def __str__(self):
        return __class__.__name__

# a = WrapperDB().get_users_coordinate(48.704578, 44.507112, 5)



class Destributor:
    def __init__(self, data):
        self.data = data

    def get_users(self):
        latitude = self.data['latitude']
        longitude = self.data['longitude'] 
        radius = self.data['radius']
        coordinate_users = WrapperDB().get_users_coordinate(latitude, longitude, radius)
        users_json = self.parsing_users(coordinate_users)
        return users_json

    def parsing_users(self, users):
        """ Parsing data in dict(dict()...) """
        try:
            new_data = dict()
            new_data['users'] = []
            for coor in users:
                new_data['users'].append([float(coor[1]), float(coor[2]), coor[0]])
            if new_data['users']:
                new_data['status'] = True
            return new_data
        except TypeError:
            return None

