import unittest
import json
import sys
sys.path[0] = sys.path[0][:-8]
from scripts.server.server import app
from scripts.logic.utilities import CommandDB


class TestApi(unittest.TestCase):
    def test_registration_2(self):
        sent = {"logmn": "bob", "pakword": 123}
        with app.test_client() as client:
            relult = client.post('url', json=sent)
            self.assertEqual(relult.json, {'info': 'incorrect data',
                                           'status': False})
 
def test_server_run():
    unittest.main()

test_server_run()
