import cv2
import os
import servo

def face_detect_demo(img):
    """
    对摄像头人脸进行识别
    :param img:图像
    :return:
    """

    global confidence
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_detector = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
    # 提取人脸的位置,并限定人脸大小100*100~300*300
    face = face_detector.detectMultiScale(gray, 1.1, 5, cv2.CASCADE_SCALE_IMAGE, (100, 100), (300, 300))

    for x, y, w, h in face:
        # 框出人脸位置
        cv2.rectangle(img, (x, y), (x + w, y + h), color=(0, 0, 255), thickness=2)

        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read('trainer/trainer.yml')
        ids, confidence = recognizer.predict(gray[y: y + h, x: x + w])

        # print('标签id:', ids, '置信评分:', confidence)

        if confidence > 70:
            cv2.putText(img, 'unkonw,无法开门', (x + 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 1)
            cv2.putText(img, str(confidence), (x + 10, y + 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 1)

        else:
            cv2.putText(img, str(names[ids - 1]), (x + 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 1)
            cv2.putText(img, str(confidence), (x + 10, y + 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 1)
            servo.moveDoor()
    cv2.imshow('result', img)


def name():
    """
    id-name对应表
    :return:
    """
    path = './facemessage'
    image_paths = [os.path.join(path, f) for f in os.listdir(path)]
    for imagePath in image_paths:
        name = str(os.path.split(imagePath)[1].split('.', 2)[1])
        names.append(name)


if __name__ == '__main__':

    cap = cv2.VideoCapture(0)
    names = []
    name()
    while True:
        flag, frame = cap.read()
        if not flag:
            print("camera not working")
            break
        face_detect_demo(frame)

        if ord(' ') == cv2.waitKey(10):
            break
    cv2.destroyAllWindows()
    cap.release()
