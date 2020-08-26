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


@app.route('/api/v0.1/add_user', methods=['POST'])
def add_user():
  data = request.json
  status = Destributor(data).add_user()
  print(status)
  return status


@app.route('/api/v0.1/delete_user', methods=['POST'])
def delete_user():
  data = request.json
  status = Destributor(data).delete_user()
  print(status)
  return status


@app.route('/api/v0.1/update_user', methods=['POST'])
def update_user():
  data = request.json
  status = Destributor(data).update_user()
  print(status)
  return status


