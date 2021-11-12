from collections import deque
import numpy as np
import argparse
import imutils
import cv2
import cam


if __name__ == '__main__':
    camera = cv2.VideoCapture(0)
    while True:
        (orange, black) = cam.read_position(camera)
        print(f'Orange = {orange} \t\t Black = {black}')
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    camera.release()
    cv2.destroyAllWindows()
