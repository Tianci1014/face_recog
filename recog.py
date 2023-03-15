
import cv2
import os


# 识别器
recognizer = cv2.face.LBPHFaceRecognizer_create()
# 加载训练数据文件
recognizer.read('trainer/trainer.yml')

# 名称
names = []


# 对输入进行识别
def face_detect_demo(img):
    # 灰度转换
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 级联分类器
    face_detector = cv2.CascadeClassifier('D:/opencv/sources/data/haarcascades/haarcascade_frontalface_alt2.xml')
    # 提取人脸的位置,并限定人脸大小100*100~300*300
    face = face_detector.detectMultiScale(gray, 1.1, 5, cv2.CASCADE_SCALE_IMAGE, (100, 100), (300, 300))

    for x, y, w, h in face:
        # 框出人脸位置
        cv2.rectangle(img, (x, y), (x + w, y + h), color=(0, 0, 255), thickness=1)

        # 人脸识别，ids是名字，confidence是评分
        ids, confidence = recognizer.predict(gray[y: y + h, x: x + w])

        print('标签id:',ids,'置信评分:',confidence)
        # 识别失败，显示unknown
        if (confidence > 80):
            # global warningtime
            # warningtime += 1
            # if warningtime > 100:
            #     # warning()  # 遇到不认识的人长时间在摄像头面前徘徊就调用报警模块
            #     warningtime = 0
            cv2.putText(img, 'unkonw', (x + 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 1)
            cv2.putText(img, str(confidence), (x + 10, y + 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 1)
        else:
            # 识别成功，显示出识别结果和置信评分
            cv2.putText(img, str(names[ids - 1]), (x + 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 1)
            cv2.putText(img, str(confidence), (x + 10, y + 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 1)
    cv2.imshow('result', img)
    # print('bug:',ids)


def name():
    path = './facemessage'
    # names = []
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    for imagePath in imagePaths:
        name = str(os.path.split(imagePath)[1].split('.', 2)[1])
        names.append(name)


cap = cv2.VideoCapture(0)
name()
while True:
    flag, frame = cap.read()
    if not flag:
        break
    face_detect_demo(frame)
    if ord(' ') == cv2.waitKey(10):  # 按空格结束
        break

face_detect_demo(frame)


cv2.destroyAllWindows()
cap.release()
# print(names)
