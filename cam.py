from collections import deque
import numpy as np
import argparse
import imutils
import cv2

orange = (5, 50, 50), (15, 255, 255)
black = (0, 0, 0), (179, 255, 50)

LOWER = 0
UPPER = 1


def read_position(camera):
    (grabbed, frame) = camera.read()

    frame = imutils.resize(frame, width=600)

    center_orange, mask_orange = _get_center(orange, frame)
    center_black, mask_black = _get_center(black, frame)

    cv2.imshow("Frame", frame)
    cv2.imshow("Mask Orange", mask_orange)
    cv2.imshow("Mask Black", mask_black)

    return (center_orange, center_black)


def _get_center(color, frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, color[LOWER], color[UPPER])
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)[-2]

    if len(cnts) > 0:
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)

        if radius > 10:
            cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
            return (x, y), mask

    return None, mask
