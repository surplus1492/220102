import cv2
import numpy as np
import serial
import time

py_serial = serial.Serial('COM5',9600)
time.sleep(2)

cap = cv2.VideoCapture(0)
ds_factor = 1.0

glass_cascade=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye_tree_eyeglasses.xml')

if glass_cascade.empty():
    raise IOError('Cannot find nose cascade classifier xml file!')

while cv2.waitKey(33) < 0:
    ret, frame = cap.read()
    frame = cv2.resize(frame, None, fx=ds_factor, fy=ds_factor, interpolation=cv2.INTER_AREA)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    eye_rects = glass_cascade.detectMultiScale(gray, 1.3, 5)
    
    txt="POWER OFF"

    for (x,y,w,h) in eye_rects:
        txt="POWER ON"
        py_serial.write(b'H')
        break
    cv2.putText(frame, txt, (180,50), cv2.FONT_HERSHEY_DUPLEX, 1.5, (255,0,0))

    py_serial.write(b'L')
    cv2.imshow("VideoFrame", frame)

else:
    py_serial.write(b'L')

cap.release()
cv2.destroyAllWindows()