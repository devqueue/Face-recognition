import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

face_cascade = cv2.CascadeClassifier('Cascades/haarcascade_frontalface_alt2.xml')

path = 'faces'
images = []
classNames = []
mylist =  os.listdir(path)
print(mylist)

for cl in mylist:
    currentImg = cv2.imread(f'{path}/{cl}')
    images.append(currentImg)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)


def findencodings(images):
    encodelist = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodelist.append(encode)
    return encodelist


encodelistknown = findencodings(images)
print(len(encodelistknown))
print("encoding complete")


cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]  # (ycord_start, ycord_end)
        roi_color = img[y:y+h, x:x+w]


    faceCurFrame = face_recognition.face_locations(imgS)

    encodesCurFrame = face_recognition.face_encodings(imgS, faceCurFrame)

    for encodeFace, faceLoc in zip(encodesCurFrame, faceCurFrame):
        matches = face_recognition.compare_faces(encodelistknown, encodeFace)
        faceDis = face_recognition.face_distance(encodelistknown, encodeFace)
        print(faceDis)
        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            print(name)
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.rectangle(img, (x1, y2-35), (x2, y2), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, name, (x1+6, y2-6),
                    cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

        # color = (255, 0, 0)  # BGR 0-255
        # stroke = 2
        # end_cord_x = x + w
        # end_cord_y = y + h
        # cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)

    cv2.imshow('Face-Detector', img)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


'''
def markattendance(name):
    with open('attendance.csv', 'r+') as f:
        dataList = f.readlines()
        nameList = []
        for line in dataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            dtstring = now.strftime('%H:%M:%S')
            f.writelines(f'\\n{name},{dtstring}')

encodelistknown = findencodings(images)
print("Encoding completed")

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    imgS = cv2.resize(img,(0,0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    faceCurFrame = face_recognition.face_locations(imgS)

    encodesCurFrame = face_recognition.face_encodings(imgS,faceCurFrame)

    for encodeFace,faceLoc in zip(encodesCurFrame, faceCurFrame):
        matches = face_recognition.compare_faces(encodelistknown, encodeFace)
        faceDis = face_recognition.face_distance(encodelistknown, encodeFace)
        #print(faceDis)
        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            #print(name)
            y1,x2,y2,x1 = faceLoc
            y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.rectangle(img,(x1,y2-35), (x2,y2), (0,255,0), cv2.FILLED)
            cv2.putText(img, name, (x1+6, y2-6), 
                        cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            markattendance('haziq')


    cv2.imshow('webcam',img)

    cv2.waitKey(1)




imghaziq = face_recognition.load_image_file('Faces/haziq.jpg')
imghaziq = cv2.cvtColor(imghaziq, cv2.COLOR_BGR2RGB)
imgTest = face_recognition.load_image_file('Faces/test.jpg')
imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)

faceloc = face_recognition.face_locations(imghaziq)[0]
encodehaziq = face_recognition.face_encodings(imghaziq)[0]
cv2.rectangle(imghaziq, 
                (faceloc[3], faceloc[0], faceloc[1], faceloc[2]),
                (255,0,255),2)

cv2.imshow('haziq', imghaziq)
cv2.imshow('haziq test', imgTest)
cv2.waitKey(0)

print("Executed successfully")
'''
