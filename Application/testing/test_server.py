import unittest
import json
import sys
sys.path[0] = sys.path[0][:-8]
from scripts.server.server import app
# from scripts.logic.utilities import CommandDB


class TestApi(unittest.TestCase):
    def test_get_user(self):
        latitude = 55.753960
        longitude = 37.620393
        radius = 10
        sent = {"latitude": latitude,
                "longitude": longitude,
                "radius": radius}
        url = r'/api/v0.1/get_users'
        with app.test_client() as client:
            relult = client.post(url, json=sent)
            self.assertIsInstance(relult.json['users'], list)
            
    # def test_add_user1(self):
    #     """Correct data submitted."""
    #     latitude = 55.753960 
    #     longitude = 37.620393
    #     sent = {"latitude": latitude, "longitude": longitude}
    #     url = r'/api/v0.1/add_user'
    #     with app.test_client() as client:
    #         relult = client.post(url, json=sent)
    #         self.assertEqual(relult.json, {'info': 'user added successfully', 'status': True})

    # def test_add_user2(self):
    #     """Not enough parameters for json."""
    #     latitude = 55.753960 
    #     sent = {"latitude": latitude}
    #     url = r'/api/v0.1/add_user'
    #     with app.test_client() as client:
    #         relult = client.post(url, json=sent)
    #         self.assertEqual(relult.json, {'info': 'invalid json', 'status': False})

    # def test_update_user1(self):
    #     """The correct data has been
    #     submitted for updating.

    #     """
    #     latitude = 55.753960 
    #     longitude = 37.620393
    #     user_id = 3
    #     sent = {"latitude": latitude,
    #             "longitude": longitude, 
    #             'user_id': user_id}
    #     url = r'/api/v0.1/update_user'
    #     with app.test_client() as client:
    #         relult = client.post(url, json=sent)
    #         self.assertEqual(relult.json, {'info': 'data changed successfully', 'status': True})
    
    # def test_update_user2(self):
    #     """Incorrect data transferred."""
    #     latitude = 55.753960 
    #     longitude = 37.620393
    #     user_id = 3
    #     sent = {"latitude": latitude,
    #             "longitude": longitude, 
    #             'qweewr': user_id}
    #     url = r'/api/v0.1/update_user'
    #     with app.test_client() as client:
    #         relult = client.post(url, json=sent)
    #         self.assertEqual(relult.json, {'info': 'invalid json', 'status': False})


def test_server_run():
    unittest.main()

test_server_run()
# СДЕЛАТЬ добовление прогона теста в MAKE