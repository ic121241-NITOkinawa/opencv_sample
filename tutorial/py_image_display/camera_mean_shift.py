# -*- coding: utf-8 -*-
import cv2
import numpy as np

cap = cv2.VideoCapture(0)
# ret = cap.set(3, 640)
# ret = cap.set(4, 480)

r,h,c,w = 250,90,400,125  # simply hardcoded the values
track_window = (c,r,w,h)
term_crit = ( cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1 )

while cap.isOpened():
    # Capture frame-by-frame
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)

    ret, track_window = cv2.CamShift(edges, track_window, term_crit)
    pts = cv2.boxPoints(ret)
    pts = np.int0(pts)
    frame = cv2.polylines(frame,[pts],True, 255,2)
    
    cv2.imshow("houghlines3.jpg", frame)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
