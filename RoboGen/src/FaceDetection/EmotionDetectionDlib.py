import cv2
import numpy as np
import dlib
from sklearn.svm import SVC
import math
import sys
from sklearn.externals import joblib
from scipy.stats import mode
import base64
import pickle
import time

# -------------------------------------------------------------------------------------------
# Set up face detection variables
# -------------------------------------------------------------------------------------------
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat") #Or set this to whatever you named the downloaded file
clf = SVC(kernel='linear', probability=True, tol=1e-3)#, verbose = True) #Set the classifier as a support vector machines with polynomial kernel
#data = {} #Make dictionary for all values
#clf = joblib.load("EmotionPredictionModel_All.sav")
#clf = joblib.load("EDModel.sav")
clf = pickle.load( open("EmotionPredictionModel_All.p", "rb"))
list_of_current_emotions = []

# -------------------------------------------------------------------------------------------
# get image from json string
# -------------------------------------------------------------------------------------------
def json2im(jstr):
    """Convert a JSON string back to a Numpy array"""
    load = json.loads(jstr)
    imdata = base64.b64decode(load['image'])
    im = pickle.loads(imdata)
    return im

# -------------------------------------------------------------------------------------------
# function decodeEmotion
# -------------------------------------------------------------------------------------------
def decodeEmotion(pred):
    if pred == 0:
        return "fear"
    elif pred == 1:
        return "happy"
    elif pred == 2:
        return "neutral"
    elif pred == 3:
        return "pain"
    elif pred == 4:
        return "sadness"
    elif pred == 5:
        return "surprise"
    else:
        return "oh well, something went wrong..."

# -------------------------------------------------------------------------------------------
# function getLandmarksForClassification
# -------------------------------------------------------------------------------------------
def getLandmarksForClassification(image):
    detections = detector(image, 1)

    for k, d in enumerate(detections): #For all detected face instances individually
        shape = predictor(image, d) #Draw Facial Landmarks with the predictor class
        xlist = []
        ylist = []
        for i in range(1, 68): #Store X and Y coordinates in two lists
            xlist.append(float(shape.part(i).x))
            ylist.append(float(shape.part(i).y))
        xmean = np.mean(xlist)
        ymean = np.mean(ylist)
        xcentral = [(x-xmean) for x in xlist]
        ycentral = [(y-ymean) for y in ylist]
        landmarks_vectorised = []
        for x, y, w, z in zip(xcentral, ycentral, xlist, ylist):
            landmarks_vectorised.append(w)
            landmarks_vectorised.append(z)
            meannp = np.asarray((ymean, xmean))
            coornp = np.asarray((z, w))
            dist = np.linalg.norm(coornp-meannp)
            landmarks_vectorised.append(dist)
            landmarks_vectorised.append((math.atan2(y, x)*360)/(2*math.pi))
            #print(len(landmarks_vectorised))
        return landmarks_vectorised

# -------------------------------------------------------------------------------------------
# keep looping endlessly to find 
# -------------------------------------------------------------------------------------------
def analyzeFrameForEmotion(frame): 

	retEmotion = "unknown"
		
	if frame is None:
		return retEmotion
	
	faces = faceCascade.detectMultiScale(frame)
	
	for (x, y, w, h) in faces:
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert image to grayscale
		face = gray[y:y + h, x:x + w]  # Cut the frame to size
		face_two = cv2.resize(face, (350, 350))
		clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
		clahe_image = clahe.apply(face_two)
		features = np.array(getLandmarksForClassification(clahe_image))
		features = np.reshape(features, (1, -1))
		
		if len(features[0]) < 100:
			continue
	
		prediction = clf.predict(features)
		list_of_current_emotions.append(prediction)
		
		if len(list_of_current_emotions) > 5:
			list_of_current_emotions.pop(0)
	
		int_emotion = mode(list_of_current_emotions)[0]
		emotion = decodeEmotion(int_emotion)
		
		#test: TODO all detected emotions of all faces should be returned, not just last one
		retEmotion = emotion
	
	return retEmotion
	
