from flask import Flask, request
from scripts.logic.utilities import Destributor
import json


app = Flask(__name__)


@app.route('/api/v0.1/get_users', methods=['POST'])
def get_users():
  try:
    data = request.json
  except KeyError:
      return {"status": False, "info": "incorrect data"}
  status = Destributor().registration()
  return {"status": status}
