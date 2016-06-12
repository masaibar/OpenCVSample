import cv2

# image_path = "images/lena.png"
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

        cv2.rectangle(image, tuple(rect[0:2]), tuple(rect[0:2] + rect[2:4]), color, thickness=2)

# 認識結果の出力
# cv2.imwrite("Lenna_result.png", image)
cv2.imshow("result", image)
cv2.waitKey(0)
