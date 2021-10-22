from collections import deque
import numpy as np
import argparse
import imutils
import cv2

orangeLower, orangeUpper = (5, 50, 50), (15, 255, 255)

camera = cv2.VideoCapture(0)

while True:
    (grabbed, frame) = camera.read()

    frame = imutils.resize(frame, width=600)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    maskOrange = cv2.inRange(hsv, orangeLower, orangeUpper)
    maskOrange = cv2.erode(maskOrange, None, iterations=2)
    maskOrange = cv2.dilate(maskOrange, None, iterations=2)

    cnts = cv2.findContours(maskOrange.copy(), cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)[-2]
    center = None

    if len(cnts) > 0:
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)

        if radius > 10:
            cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)

    cv2.imshow("Frame", frame)
    cv2.imshow("Mask Orange", maskOrange)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
