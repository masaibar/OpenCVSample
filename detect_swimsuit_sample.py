# -*- coding:utf-8 -*-
import cv2
import numpy as np
from pprint import pprint

# image_path = "images/lena.png"
# IMAGE_PATH = "images/kojiruri.png"
# IMAGE_PATH = "images/picture.jpg"
IMAGE_PATH = "images/picture2.jpg"
CASCADE_PATH = "haarcascades/haarcascade_frontalface_alt.xml"

def detect_faces(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cascade = cv2.CascadeClassifier(CASCADE_PATH)
    return cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=1, minSize=(70, 70))

def detect_swimsuit(image, swimsuit_areas):
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lowerb = np.array([0, 180, 8])
    upperb = np.array([360, 255, 247])
    swimsuit = cv2.inRange(src=hsv_image, lowerb=lowerb, upperb=upperb)
    _, contours, _ = cv2.findContours(image=swimsuit, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if contour.size < 25:
            continue

        # pprint(contour)
        swimsuit_areas.append(contour)

    result = cv2.drawContours(image=image, contours=swimsuit_areas, contourIdx=-1, color=(255,255,255), thickness=2)
    return result
    # return hsv_image


def main():
    image = cv2.imread(IMAGE_PATH)
    swimsuit_areas = []

    faces = detect_faces(image)

    result = detect_swimsuit(image, swimsuit_areas)
    print(swimsuit_areas)

    cv2.imshow("result", result)
    # cv2.imshow("original", image)
    cv2.waitKey(5000)

if __name__ == "__main__":
    main()