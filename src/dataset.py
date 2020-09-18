import cv2
import numpy
import os

face_cascade = cv2.CascadeClassifier('Cascades/haarcascade_frontalface_alt2.xml')
name = input("Enter your name: ")
count = 0
cap = cv2.VideoCapture(0)

def face_ext(img):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)

    if faces is():
        return None

    for(x,y,w,h) in faces:
        cropped_face = img[y:y+h, x:x+w]

    return cropped_face



while True:
    re, frame = cap.read()
    if face_ext(frame) is not None:
        count+=1
        face = cv2.resize(face_ext(frame), (200,200))
        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
        path = os.path.join('images/', f'{name}')
        file_path = os.path.join(path ,str(count) + '.jpg')
        print(file_path)
        if not os.path.exists(path):
            os.mkdir(path)
        elif os.path.exists(path):
            cv2.imwrite(file_path, face)
        
        cv2.putText(face, str(count), (50,50), cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,255,0),2)
        cv2.imshow('Data Collector', face)

    else:
        pass

    if cv2.waitKey(1) == 13 or count==100:
        break

cap.release()
cv2.destroyAllWindows()
print("Dataset Collection Completed")
