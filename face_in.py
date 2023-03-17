"""
此文件用于向数据库添加人脸信息
"""
import cv2
import os
import numpy as np
import text_in


def image_name():
    """
    获取新增人脸的文件名（即人脸的label）
    :return: (文件名，ID)
    """

    path = "./facemessage"
    files = os.listdir(path)
    num = len(files)
    # name = input('please enter your name:')
    name = text_in.collect_name()
    id = num + 1
    image_name = str(id) + '.' + name + '.png'
    return image_name, id


def cv2_image_camera():
    """
    拍照收集照片数据并自动保存
    :param name:文件名
    :return: 图像
    """
    name ,id = image_name()
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        # frame = cv2.flip(frame,1)
        # 按下q键退出程序
        cv2.imshow('face_message_collect', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.imwrite('./facemessage/' + name, frame)
            break
    # 释放资源w
    cap.release()
    cv2.destroyAllWindows()
    return frame


#
# def train_image(frame):
#     """
#     :param frame: 图片
#     :return: 图片中人脸部分的数组
#     """
#     # 将图片转化为灰度图片再转化为数组
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     image_numpy = np.array(gray)
#
#     # 级联分类器,接受数据集，作用是定位输入照片的人脸
#     face_detector = cv2.CascadeClassifier('D:/opencv/sources/data/haarcascades/haarcascade_frontalface_alt2.xml')
#     # 将数组传入，只取人脸的部分
#     faces = face_detector.detectMultiScale(image_numpy)
#     for x, y, w, h in faces:
#         # 人脸信息即脸部分的数组
#         face_data = image_numpy[y:y + h, x:x + w]
#
#     return face_data

#
# name, id = image_name()
#
# frame = cv2_image_camera(name)
# face = train_image(frame)
# # print(id)
# # print(face)
#
# # 加载识别器，LBPH特征算法类
# recognizer = cv2.face.LBPHFaceRecognizer_create()
# # 训练
# id = [id]
# face = [face]
# recognizer.train(face, np.array(id))
# # 保存文件
# recognizer.write('trainer/trainer_2.yml')

if  __name__ == '__main__':
    cv2_image_camera()
