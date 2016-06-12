# -*- coding:utf-8 -*-
import cv2
import numpy as np

#画像処理入門講座 : OpenCVとPythonで始める画像処理 | プログラミング | POSTD : http://postd.cc/image-processing-101/

# IMAGE_PATH = "images/lena.png"
# IMAGE_PATH = "images/kojiruri.png"
IMAGE_PATH = "images/picture.jpg"
IMAGE_PATH = "images/picture2.jpg"
# IMAGE_PATH = "images/picture3.jpg"
CASCADE_PATH = "haarcascades/haarcascade_frontalface_alt.xml"

def detect_faces(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cascade = cv2.CascadeClassifier(CASCADE_PATH)
    return cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=1, minSize=(70, 70))

def detect_skin_area(image, skin_areas):
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lowerb = np.array([3, 30, 0], np.uint8)
    upperb = np.array([30, 150, 240], np.uint8)
    hadairo_image = cv2.inRange(hsv_image, lowerb, upperb)
    hadairo_image = cv2.cvtColor(hadairo_image, cv2.COLOR_GRAY2RGB)

    kernel = np.ones((2,2), np.uint8)
    hadairo_image = cv2.dilate(hadairo_image, kernel, iterations=1)
    hadairo_image = cv2.dilate(hadairo_image, kernel, iterations=1)

    return hadairo_image #ココで返す

def main():
    image = cv2.imread(IMAGE_PATH)

    faces = detect_faces(image)
    print(faces)

    skin_areas = []
    result = detect_skin_area(image, skin_areas)

    cv2.imshow("result", result)
    # cv2.imshow("original", image)
    cv2.waitKey(10000)

if __name__ == "__main__":
    main()