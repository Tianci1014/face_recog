import datetime
import os
from os import listdir
import cv2
from PIL import Image
import numpy as np

"""
此文件用于更新照片库的识别信息，对所有照片进行重新扫描与识别，产生所有人脸及对应标签，并以此训练，生成特征数据
"""


def getImageAndLabels():
    """
    对数据库所有照片进行
    :return: 人脸数组，标签
    """

    # 人脸数组列表和标签列表
    face_samples = []
    ids = []

    path = "./facemessage"
    imagePaths = [os.path.join(path, f) for f in listdir(path)]

    # 遍历列表中的图片
    for imagePaths in imagePaths:

        pil_img = Image.open(imagePaths).convert('L')
        img_numpy = np.array(pil_img, 'uint8')

        face_detector = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
        face = face_detector.detectMultiScale(img_numpy)

        ids = int(os.path.split(imagePaths)[1].split('.')[0])

        #  x, y, w, h给出了人脸的位置信息
        for x, y, w, h in face:
            ids.append(ids)
            face_samples.append(img_numpy[y:y + h, x:x + w])
    # 打印id和面部特征
    # print('id:', id)
    # print('fs:', faceSamples)
    return face_samples, ids


def train():
    """
    自动获取数据并训练，生成识别文件
    :return:
    """
    face_samples, ids = getImageAndLabels()

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.train(face_samples, np.array(ids))
    recognizer.write('trainer/trainer.yml')


if __name__ == '__main__':
    train()
