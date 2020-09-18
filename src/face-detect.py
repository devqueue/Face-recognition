import numpy as np
import cv2
import pickle
import face_recognition
import os
from datetime import datetime

face_cascade = cv2.CascadeClassifier('Cascades/haarcascade_frontalface_alt2.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()

recognizer.read("./recognizer/face-trainner.yml")


def markattendance(name):
    with open('Attendance.csv', 'r+') as f:
        dataList = f.readlines()
        nameList = []
        for line in dataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            date = now.strftime('%b %d %Y')
            day = now.strftime('%a')
            time = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name}, {date}, {time}, {day}')            



labels = {"person_name": 1}
with open("pickles/face-labels.pickle", 'rb') as f:
	og_labels = pickle.load(f)
	labels = {v: k for k, v in og_labels.items()}


cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
    	gray, scaleFactor=1.5, minNeighbors=5)
    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]  # (ycord_start, ycord_end)
        roi_color = frame[y:y+h, x:x+w]

    	# recognize
        id_, conf = recognizer.predict(roi_gray)
        if conf >= 4 and conf <= 85:
            font = cv2.FONT_HERSHEY_SIMPLEX
            name = labels[id_]
            color = (255, 255, 255)
            stroke = 2
            #cv2.rectangle(frame, (x+45, y+35), (x, y), (0, 255, 0), cv2.FILLED)
            cv2.putText(frame, name, (x, y), font,1, color, stroke, cv2.FILLED)
            markattendance(name)

            #img_item = "7.png"
            #cv2.imwrite(img_item, roi_color)

        color = (0, 255, 0)  # BGR 0-255
        stroke = 2
        end_cord_x = x + w
        end_cord_y = y + h
        cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)
    	#subitems = smile_cascade.detectMultiScale(roi_gray)
    	#for (ex,ey,ew,eh) in subitems:
    	#	cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    # Display the resulting frame
    cv2.imshow('Face-detector', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

