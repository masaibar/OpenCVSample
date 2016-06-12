# -*- coding:utf-8 -*-

import cv2
import numpy as np
from PolkaDot import PolkaDot


class PolkaDotsCollage:
    def __init__(self, image_path):
        self.image = cv2.imread(image_path)
        self.polka_dots = []
        self.faces = []

    def detect_faces(self):
        CASCADE_PATH = "haarcascades/haarcascade_frontalface_alt.xml"

        image_gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        cascade = cv2.CascadeClassifier(CASCADE_PATH)
        self.faces = cascade.detectMultiScale(image_gray, scaleFactor=1.1, minNeighbors=1, minSize=(1, 1))

    def create_polka_dot(self):
        for x, y, w, h in self.faces:
            center_x = int(x + w / 2)
            center_y = int(y + h / 2)
            radius = int(np.sqrt(np.power(h / 2, 2) + np.power(w / 2, 2)))
            polka_dot = PolkaDot(center_x, center_y, radius)
            if polka_dot is not None:
                self.polka_dots.append(polka_dot)

    def draw_masked_image(self):
        height, width = self.image.shape[:2]
        print("[Size] Height = %d, Width = %d" % (height, width))

        # maskをかける
        mask = np.zeros((height, width), np.uint8)

        # 水玉模様になる園の定義
        for polka_dot in self.polka_dots:
            print(polka_dot.get_center())
            print(polka_dot.get_radius())
            cv2.circle(mask, polka_dot.get_center(), polka_dot.get_radius(), 255, -1)

        masked_image = cv2.bitwise_and(self.image, self.image, mask=mask)
        cv2.imshow("masked", masked_image)
        cv2.waitKey(0)

    def show(self):
        cv2.waitKey(0)

    def exec(self):
        self.detect_faces()
        self.create_polka_dot()
        self.draw_masked_image()
