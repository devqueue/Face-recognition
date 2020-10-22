import cv2
import os
import string
from random import randint

def get_random_string(length):
    # Random string with the combination of lower and upper case
    letters = string.ascii_letters
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def Photocambw():
    cam = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier('Cascades/haarcascade_frontalface_alt2.xml')
    name = input("Enter your name: ")
    pics = int(input("No. of images: "))
    suffix = get_random_string()
    k = cv2.waitKey(100) & 0xff

    print("\n [INFO] Initializing face capture. Look the camera and wait ...")


    def face_ext(img):
        gray = frame
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)

        if faces is():
            return None

        for(x,y,w,h) in faces:
            cropped_face = img[y:y+h, x:x+w]

        return cropped_face



    while True:
        _re, frame = cam.read()
        if face_ext(frame) is not None:
            count+=1
            face = cv2.resize(face_ext(frame), (200,200))
            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
            path = os.path.join('captured/', f'{name}')
            file_path = os.path.join(path ,str(suffix) + '.jpg')
            print(file_path)
            if not os.path.exists(path):
                os.mkdir(path)
            elif os.path.exists(path):
                cv2.imwrite(file_path, face)
            
            cv2.putText(face, str(count), (50,50), cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,255,0),2)
            cv2.imshow('Data Collector', face)

        else:
            pass

        if k == 27 or count==pics:
            break
    print("\n[INFO] Exiting Program and cleanup stuff")
    cap.release()
    cv2.destroyAllWindows()
    print("Dataset Collection Completed")
