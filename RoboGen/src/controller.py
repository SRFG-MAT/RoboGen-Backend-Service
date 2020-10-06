
#----------------------------------------------------
# RoboGen-Backend-Service
# Author: Mathias Schmoigl
# Creation Date: 23.10.2019
#----------------------------------------------------
from flask import Flask,request,jsonify
import logging
import json
from EmotionDetectionDlib import *
from DataBaseHandler import *

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

#----------------------------------------------------
# API function to show welcome string
#----------------------------------------------------
@app.route("/")
def showServiceStatus():
    return "RoboGen-Backend-Service: Running"

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
# API fucntion to post an image of QBO for face detection
# and receive an interpreted emotion as a string
#----------------------------------------------------
@app.route("/FaceDetection/AnalyzeFrameForEmotion", methods=['POST'])
def analyzeFrameForEmotion():

    emotion = "unknown"
    readable_json = json.loads(request.json)
    imageDecoded = readable_json['image']
    image = json2im(imageDecoded)
    logger.info('analyzing frame for emotion')

    # analyze this frame and return the results delimitted by the character "-"
    retEmotion, retCamCode = analyzeFrame(image)
    return '{}-{}'.format(retEmotion, retCamCode)


#----------------------------------------------------
# API function to send JSON files to database
#----------------------------------------------------
@app.route("/DataBase/UploadJSON_MyCalendar", methods=['POST'])
def uploadJSONMyCalendar():

    readable_json = json.loads(json.dumps(request.json))
    storeMyCalendar(readable_json)
    return '{"response":"Server stored entry succesfully"}'

#----------------------------------------------------
# API function to receive JSON files from database
#----------------------------------------------------
@app.route("/DataBase/DownloadJSON_MyCalendar", methods=['POST'])
def downloadJSONMyCalendar():
    return loadMyCalendar()

#----------------------------------------------------
# API function to delete/reset JSON files from database
#----------------------------------------------------
@app.route("/DataBase/ResetJSON_MyCalendar", methods=['POST'])
def resetJSONMyCalendar():
    resetMyCalendar()
    return '{"response":"Server reset calendar succesfully"}'

#----------------------------------------------------
# API function to send JSON files to database
#----------------------------------------------------
@app.route("/DataBase/EditJSON_MyCalendar", methods=['POST'])
def editJSONMyCalendar():

    readable_json = json.loads(json.dumps(request.json))
    editMyCalendar(readable_json)
    return '{"response":"Server edited entry succesfully"}'









