# -*- coding:utf-8 -*-
import cv2
import numpy as np

# image_path = "images/lena.png"
# image_path = "images/2girls.png"
image_path = "images/kojiruri.png"
image = cv2.imread(image_path);
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cascade_path = "haarcascades/haarcascade_frontalface_alt.xml"

cascade = cv2.CascadeClassifier(cascade_path)

facerecog = cascade.detectMultiScale(image_gray, scaleFactor=1.1, minNeighbors=1, minSize=(1, 1))

color = (255, 255, 255)

if len(facerecog) > 0:

    # 認識した顔全てを矩形で囲む
    for rect in facerecog:
        # 認識結果を表示
        print("認識結果")
        print("(x,y)=(" + str(rect[0]) + "," + str(rect[1]) + ")" + \
              "  高さ：" + str(rect[2]) + \
              "  幅：" + str(rect[3]))

        print(rect[0:2] + rect[2:4])
        print(rect[0])
        print(rect[1])
        print(rect[2])
        print(rect[3])
        rect_x = rect[0]
        rect_y = rect[1]
        rect_h = rect[2]
        rect_w = rect[3]

        center_x = int(rect_x + rect_w / 2)
        center_y = int(rect_y + rect_h / 2)
        center = (center_x, center_y)

        # radius = 30
        radius = int(np.sqrt(np.power(rect_h / 2, 2) + np.power(rect_w / 2, 2)))

        color = (255, 255, 255)

        cv2.rectangle(image, tuple(rect[0:2]), tuple(rect[0:2] + rect[2:4]), color, thickness=1) #debug rect
        cv2.circle(image, center, radius, color, thickness=1) #circle

# 認識結果の出力
# cv2.imwrite("Lenna_result.png", image)
cv2.imshow("result", image)
cv2.waitKey(0)
