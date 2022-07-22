from collections import deque
import argparse
import cv2


class Color:
    def __init__(self, lower, upper):
        self.lower = lower
        self.upper = upper


crop_offset = (5, 110)
crop_size = 410
scale = 0.5
center = (crop_size * scale / 2, crop_size * scale / 2)


class Camera:
    def __init__(self, cid=0, show_windows=False):
        self.camera = cv2.VideoCapture(cid)
        self.set_resolution(640, 480)

        self.orange = Color((5, 50, 50), (15, 255, 255))
        self._show_windows = show_windows

    def read_position(self):
        (grabbed, frame) = self.camera.read()
        frame = self._rescale(self._crop(frame))

        c_black = None
        c_orange = self._get_center(self.orange, frame)

        if self._show_windows:
            cv2.imshow("Frame", frame)

        return c_orange

    def release(self):
        self.camera.release()
        cv2.destroyAllWindows()

    def set_resolution(self, width, height):
        self.camera.set(3, width)
        self.camera.set(4, height)

    def _rescale(self, frame):
        frame = cv2.resize(frame,
                           (int(frame.shape[0] * scale), int(frame.shape[1] * scale)))
        return frame

    def _crop(self, frame):
        xstart = crop_offset[0]
        xend = xstart + crop_size
        ystart = crop_offset[1]
        yend = ystart + crop_size
        return frame[xstart:xend, ystart:yend]

    def _get_center(self, color, frame):
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, color.lower, color.upper)
        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)

        cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[-2]

        if len(cnts) > 0:
            c = max(cnts, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(c)

            if radius < 5:
                return None

            if self._show_windows:
                cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)

            return (x, y)

        return None


if __name__ == '__main__':
    cam = Camer(show_windows=True)

    while True:
        cam.read_position()
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
