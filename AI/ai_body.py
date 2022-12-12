import cv2
import numpy as np

cap = cv2.VideoCapture(0)
ds_factor = 1.0

body_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_fullbody.xml')
leg_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_lowerbody.xml')
upper_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_upperbody.xml')

if body_cascade.empty():
    raise IOError('Cannot find nose cascade classifier xml file!')
if leg_cascade.empty():
    raise IOError('Cannot find nose cascade classifier xml file!')
if upper_cascade.empty():
    raise IOError('Cannot find nose cascade classifier xml file!')

while cv2.waitKey(33) < 0:
    ret, frame = cap.read()
    frame = cv2.resize(frame, None, fx=ds_factor, fy=ds_factor, interpolation=cv2.INTER_AREA)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    body_rects = body_cascade.detectMultiScale(gray, 1.3, 5)
    leg_rects = leg_cascade.detectMultiScale(gray, 1.3, 5)
    upper_rects = upper_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in body_rects:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 3) #초록
        break
    for (x,y,w,h) in leg_rects:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 3) #파랑
        break
    for (x,y,w,h) in upper_rects:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,0,255), 3) #빨강
        break

    cv2.imshow("VideoFrame", frame)

cap.release()
cv2.destroyAllWindows()