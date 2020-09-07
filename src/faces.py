
import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('Cascades/haarcascade_frontalface_alt2.xml')

cap = cv2.VideoCapture(0)

while(True):
    #capture frame by frame
    ret, frame = cap.read()
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(grey, scaleFactor=1.5, minNeighbors=5)
    for (x, y, w, h) in faces:
        #print(x, y, w, h)
        roi_grey = grey[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        #recognizer
        

        #img_item = "my-image.png"   
        #cv2.imwrite(img_item, roi_grey)   #writes images to disk

        #rectangle
        color = (255, 0, 0) #BGR NOT RGB
        stroke = 2
        end_cord_x = x+w
        end_cord_y = y + h
        cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)



    #display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

    #release everything
cap.release()
cv2.destroyAllWindows()
print("Execution completed")
