from collections import deque
import argparse
import imutils
import cv2


class Color:
    def __init__(self, lower, upper):
        self.lower = lower
        self.upper = upper


class Camera:
    def __init__(self, cid=0, show_windows=False):
        self.camera = cv2.VideoCapture(cid)
        self.black = Color((0, 0, 0), (179, 255, 50))
        self.orange = Color((5, 50, 50), (15, 255, 255))
        self._show_windows = show_windows

    def read_position(self, colors='all'):
        (grabbed, frame) = self.camera.read()
        frame = imutils.resize(frame, width=600)

        c_orange, mask_orange = self._get_center(self.orange, frame)
        c_black, mask_black = self._get_center(self.black, frame)

        if self._show_windows:
            cv2.imshow("Frame", frame)
            cv2.imshow("Mask Orange", mask_orange)
            cv2.imshow("Mask Black", mask_black)

        if colors == 'all':
            return (c_orange, c_black)
        if colors == 'orange':
            return c_orange
        if colors == 'black':
            return c_black

    def release():
        self.camera.release()
        cv2.destroyAllWindows()

    def _get_center(self, color, frame):
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, color.lower, color.upper)
        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)

        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
                                cv2.CHAIN_APPROX_SIMPLE)[-2]

        if len(cnts) > 0:
            c = max(cnts, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(c)

            if radius > 10:
                if self._show_windows:
                    cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
                return (x, y), mask

        return None, mask
