from flask import Flask, request
from scripts.logic.utilities import Destributor
from scripts.logic.utilities import WrapperDB
import json


app = Flask(__name__)


@app.route('', methods=['POST'])
def registration():
    try:
      pass
    except KeyError:
        return {"status": False, "info": "incorrect data"}
    user = Destributor()
    status = user.registration()
    return {"status": status}
