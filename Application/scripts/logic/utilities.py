import os
import json
import psycopg2
import requests
import folium
from folium.plugins import MarkerCluster


class Atlas:
    """Processes a list of coordinates
    and draws them on the map.

    """
    def __init__(self, latitude, longitude, radius):
        self.latitude = latitude
        self.longitude = longitude
        self.zoom_start = self.zoom_handler(radius)
        self.map = folium.Map(location=[latitude,longitude], zoom_start = 11)
        self.marker_cluster = MarkerCluster().add_to(self.map)
        print(self.marker_cluster)
    
    def generation_map(self, coordinates):
        """Draws coordinates on the map."""
        for point in coordinates['users']:
            lat, lon, info_id = point
            print(point)
            folium.Marker(location=[lat,lon], popup=info_id, icon=folium.Icon(color = 'gray')).add_to(self.marker_cluster)
        return self.map

    def zoom_handler(self, radius):
        """Calculates a suitable zoom."""
        if radius > 40:
            return 10
        if 20 < radius < 40:
            return 11
        return 12
        

class ConnectDB():
    """Class for connect to DB."""
    def __init__(self):
        self.conn = psycopg2.connect(**self.config_app()['Data_Base'])
        self.cursor = self.conn.cursor()

    def config_app(self):
        path = os.getcwd() + "/Application/config.json"
        with open(path) as config:
            json_str = config.read()
            return json.loads(json_str)

    def close(self):
        self.conn.close()
        self.cursor.close()


class WrapperDB:
    """Class for requests DB."""
    def __init__(self):
        self.connect_db = ConnectDB()

    def get_users_coordinate(self, center_lat, center_lon, radius):
        """Returns a sheet with coordinates 
        included in the desired radius
        center_lat, center_lon - latitude and longitude in radians
        radius - in kilometers.

        """
        request = f"""SELECT id, Lat, Lon
                    FROM coordinate
                    WHERE acos(sin(radians({center_lat}))*sin(radians(Lat)) + cos(radians({center_lat}))*cos(radians(Lat))*cos(radians(Lon)-radians({center_lon}))) * 6371 < {radius}
                    """
        self.connect_db.cursor.execute(request)
        return self.connect_db.cursor.fetchall()

    def add_user(self, latitude, longitude):
        """Writes coordinates to the database."""
        request = f"INSERT INTO coordinate (Lat, Lon) VALUES({latitude}, {longitude})"
        self.connect_db.cursor.execute(request)
        self.connect_db.conn.commit()
        if self.connect_db.cursor.statusmessage == "INSERT 0 1":
            return True
        return False

    def delete_user(self, user_id):
        """Removing a user by his ID."""
        request = f"DELETE FROM coordinate WHERE Id = '{user_id}'"
        self.connect_db.cursor.execute(request)
        self.connect_db.conn.commit()
        if self.connect_db.cursor.statusmessage == "DELETE 1":
            return True
        return False
    
    def update_user(self, latitude, longitude, user_id):
        """
        """
        request = f"""UPDATE coordinate 
                        SET Lat = '{latitude}',
                            Lon = '{longitude}'
                        WHERE(Id = '{user_id}')"""
        self.connect_db.cursor.execute(request)
        self.connect_db.conn.commit()
        if self.connect_db.cursor.statusmessage == "UPDATE 1":
            return True
        return False

    def __str__(self):
        return __class__.__name__


class Destributor:
    """Serves as a layer between the 
    server and the database.

    """
    def __init__(self, data):
        self.data = self.handler_data(data)

    def handler_data(self, data):
        latitude = data.get('latitude')
        longitude = data.get('longitude')
        radius = data.get('radius')
        data['flag'] = True
        try:
            if latitude:
                latitude = float(latitude)
                if latitude < 0 or latitude > 90:
                    data['flag'] = False
            if longitude:
                longitude = float(longitude)
                if longitude < 0 or longitude > 180:
                    data['flag'] = False
            if radius:
                radius = int(radius)
                if radius > 100:
                    data['flag'] = False
        except ValueError:
            data['flag'] = False
        finally:
            return data

    def get_users(self):
        """Displaying the nearest neighbors to the 
        given coordinates of longitude and 
        latitude within a radius of N kilometers.

        """
        if self.data['flag']:
            try:
                latitude = self.data['latitude']
                longitude = self.data['longitude'] 
                radius = self.data['radius']
            except (AttributeError, TypeError, ValueError, KeyError):
                return {"status": False, "info": "invalid json"}
            coordinate_users = WrapperDB().get_users_coordinate(latitude, longitude, radius)
            users_json = self.parsing_users(coordinate_users)
            return users_json
        return {"status": False, "info": "invalid json data"}

    def parsing_users(self, users):
        """Parsing data in 
        {'status': True, 
        'users':[lat, lon, id],[...]...}
        if None.

        """
        try:
            new_data = dict()
            new_data['users'] = []
            for coor in users:
                new_data['users'].append([float(coor[1]), float(coor[2]), coor[0]])
            return new_data
        except TypeError:
            return {"status": False, "info": "json collection error"}
        else:
            new_data['status'] = True

    def add_user(self):
        """Allows you to add a new user."""
        if self.data['flag']:
            try:
                latitude = self.data['latitude']
                longitude = self.data['longitude']
            except (AttributeError, TypeError, ValueError, KeyError):
                return {"status": False, "info": "invalid json"}
            status = WrapperDB().add_user(latitude, longitude)
            if status:
                return {"status": True, "info": "user added successfully"}
            return {"status": False, "info": "error, user is not logged"}
        return {"status": False, "info": "invalid json data"}
    
    def delete_user(self):
        """Allows you to delete user."""
        try:
            user_id = self.data['user_id']
        except (AttributeError, TypeError, ValueError, KeyError):
            return {"status": False, "info": "invalid json"}
        status = WrapperDB().delete_user(user_id) 
        if status:
            return {"status": True, "info": "user deleted successfully"}
        return {"status": False, "info": "error, user not deleted"}
    
    def update_user(self):
        """Allows you to update user."""
        if self.data['flag']:
            try:
                user_id = self.data['user_id']
                latitude = self.data['latitude']
                longitude = self.data['longitude']
            except (AttributeError, TypeError, ValueError, KeyError):
                return {"status": False, "info": "invalid json"}
            status = WrapperDB().update_user(latitude, longitude, user_id)
            if status:
                return {"status": True, "info": "data changed successfully"}
            return {"status": False, "info": "error, data not changed"}
        return {"status": False, "info": "invalid json data"}

    def web_get_map(self):
        """Returns html if correct data."""
        if self.data['flag']:
            try:
                radius = int(self.data['radius'])
                latitude = float(self.data['latitude'])
                longitude = float(self.data['longitude'])
            except (AttributeError, TypeError, ValueError, KeyError):
                return {"status": False, "info": "invalid json"}
            print(radius, latitude, longitude)
            coordinate_users = WrapperDB().get_users_coordinate(latitude, longitude, radius)
            if not coordinate_users:
                return {"status": "not_point", "info": "invalid json data"}
            users_json = self.parsing_users(coordinate_users)
            maps = Atlas(latitude, longitude, radius).generation_map(users_json)
            return maps
        return {"status": False, "info": "invalid json data"}
