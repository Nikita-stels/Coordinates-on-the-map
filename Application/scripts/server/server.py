from flask import Flask, request
from scripts.logic.utilities import Destributor
import json


app = Flask(__name__)


@app.route('/api/v0.1/get_users', methods=['POST'])
def get_users():
  data = request.json
  status = Destributor(data).get_users()
  print(status)
  return status
