from flask import Flask, request
from flask import render_template
from flask_cors import CORS
from scripts.logic.utilities import Destributor
import json


app = Flask(__name__)
CORS(app)

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


@app.route('/api/v2/web_get_users/', methods=['GET', 'POST'])
def web_get_users():
  print(request.json)
  return render_template('index.html')


@app.route('/api/v2/web_get_map/', methods=['POST'])
def web_get_map():
  data = request.json
  status = Destributor(data).web_get_map()
  print(status)
  if isinstance(status, dict):
    return status
  return status._repr_html_()
