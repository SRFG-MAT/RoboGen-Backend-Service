
#----------------------------------------------------
# RoboGen-Backend-Service
# Author: Mathias Schmoigl
# Creation Date: 23.10.2019
#----------------------------------------------------
from flask import Flask,request,jsonify
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

#----------------------------------------------------
# API function to post a name using JSON
#----------------------------------------------------
@app.route('/v1/api', methods=['POST'])
def postSomeThing():
    content = request.json
    name = content['name']
    logger.info('name: %s',name)
    return "Hello %s" %name

#----------------------------------------------------
# API function to show hello world
#----------------------------------------------------
@app.route("/")
def hello():
    return "Hello World!"
