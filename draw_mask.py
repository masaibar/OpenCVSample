# -*- coding:utf-8 -*-
import cv2
import numpy as np

# image_path = "images/lena.png"
# image_path = "images/2girls.png"
image_path = "images/kojiruri.png"
image = cv2.imread(image_path);


CASCADE_PATH = "haarcascades/haarcascade_frontalface_alt.xml"
color = (255, 255, 255)

#認識した顔を返す
def detect_faces(image):
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cascade = cv2.CascadeClassifier(CASCADE_PATH)
    return cascade.detectMultiScale(image_gray, scaleFactor=1.1, minNeighbors=1, minSize=(1, 1))

def draw_rect(facerecog):
    if len(facerecog) < 1:
        print("認識なし")
        return

    # 認識した顔全てを矩形で囲む
    for rect in facerecog:
        rect_x = rect[0]
        rect_y = rect[1]
        rect_h = rect[2]
        rect_w = rect[3]

        # 認識結果を表示
        print("認識結果")
        print("(x,y)=(" + str(rect_x) + "," + str(rect_y) + ")" + \
              "  高さ：" + str(rect_h) + \
              "  幅：" + str(rect_w))
        cv2.rectangle(image, tuple(rect[0:2]), tuple(rect[0:2] + rect[2:4]), color, thickness=1)  # debug rect


def draw_circle(facerecog):
    if len(facerecog) < 1:
        print("認識なし")
        return

    for rect in facerecog:
        rect_x = rect[0]
        rect_y = rect[1]
        rect_h = rect[2]
        rect_w = rect[3]

        center_x = int(rect_x + rect_w / 2)
        center_y = int(rect_y + rect_h / 2)
        center = (center_x, center_y)

        radius = int(np.sqrt(np.power(rect_h / 2, 2) + np.power(rect_w / 2, 2)))
        cv2.circle(image, center, radius, color, thickness=1)  # circle

def draw_mask():
    height, width = image.shape[:2]
    print("[Size] Height = %d, Width = %d" % (height, width))

    mask = np.zeros((height, width), np.uint8)
    cv2.circle(mask, (100, 100), 30, 255, -1)
    # cv2.imshow("mask", mask)

    masked_image = cv2.bitwise_and(image, image, mask=mask)
    cv2.imshow("masked_image", masked_image)

    return masked_image


#認識した顔たちを取得
facerecog = detect_faces(image)

#矩形を描画
# draw_rect(facerecog)

#円を描画
# draw_circle(facerecog)

#mask処理を行う
result = draw_mask()

# 認識結果の出力
# cv2.imwrite("Lenna_result.png", image)
# cv2.imshow("result", image)
cv2.imshow("result", result)
cv2.waitKey(0)
