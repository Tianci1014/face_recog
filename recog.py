import time

import cv2
import os

# import servo
"""
该文件的人脸识别为摄像头不断获取照片并对照片进行人脸识别
照片逐帧返回形成视频的假象

"""


def face_detect_demo(img):
    """
    对输入的图像进行识别
    :param img:图像
    :return:
    """

    global isRight

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_detector = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
    face = face_detector.detectMultiScale(gray, 1.1, 5, cv2.CASCADE_SCALE_IMAGE, (100, 100), (300, 300))

    for x, y, w, h in face:
        # 框出人脸位置
        cv2.rectangle(img, (x, y), (x + w, y + h), color=(0, 0, 255), thickness=2)

        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read('trainer/trainer.yml')

        id, confidence = recognizer.predict(gray[y: y + h, x: x + w])

        if confidence > 70:
            isRight = False
            cv2.putText(img, 'unkonw', (x + 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 1)
            cv2.putText(img, str(confidence), (x + 10, y + 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 1)

        else:
            isRight = True
            cv2.putText(img, getName()[id], (x + 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 1)
            cv2.putText(img, str(confidence), (x + 10, y + 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 1)
            # servo.moveDoor()

    # 展示图像
    cv2.imshow('result', img)


# def name():
#     """
#     id-name查询表
#     :return:
#     """
#     path = './facemessage'
#     image_paths = [os.path.join(path, f) for f in os.listdir(path)]
#     for imagePath in image_paths:
#         name = str(os.path.split(imagePath)[1].split('.', 2)[1])
#         names.append(name)


def getName():
    """
    从图片的标签获取姓名
    :return:
    """
    Name = {}
    path = './facemessage'
    for image in os.listdir(path):
        id = int(image.split('.')[0])
        name = image.split('.')[1]
        Name[id] = name
    return Name


if __name__ == '__main__':

    cap = cv2.VideoCapture(0)

    isRight = False

    while True:
        flag, frame = cap.read()
        if not flag:
            print("camera not working")
            break
        face_detect_demo(frame)
        if isRight == True:
            print("开门")
        else:
            print("拒绝开门")

        if ord(' ') == cv2.waitKey(10):
            break

    cv2.destroyAllWindows()
    cap.release()
