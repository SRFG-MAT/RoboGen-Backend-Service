
#----------------------------------------------------
# RoboGen-Backend-Service
# Author: Mathias Schmoigl
# Creation Date: 23.10.2019
#----------------------------------------------------
from flask import Flask,request,jsonify
import logging
import json
from EmotionDetectionDlib import *

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
	
	# analyze this frame and return the result
	return analyzeFrameForEmotion(image)
