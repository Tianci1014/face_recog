
import datetime
import os
import cv2
from PIL import Image
import numpy as np


def getImageAndLabels(path):
    """
    将照片组交给级联分类器，级联分类器给出人脸数组与标签
    :return: 人脸数组，标签
    """

    face_samples = []
    ids = []

    for imagePaths in os.listdir(path):

        pil_img = Image.open(os.path.join(path, imagePaths)).convert('L')
        img_numpy = np.array(pil_img, 'uint8')

        face_detector = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
        face = face_detector.detectMultiScale(img_numpy)

        id = int(imagePaths.split('.')[0])

        for x, y, w, h in face:
            ids.append(id)
            face_samples.append(img_numpy[y:y + h, x:x + w])

    return face_samples, ids


def train(face_samples, ids):
    """
    将样本与标签交给训练器训练，训练器生成存有特征数据的文件
    :return:
    """
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.train(face_samples, np.array(ids))
    recognizer.write('trainer/trainer.yml')


if __name__ == '__main__':
    path = "./facemessage"
    face_samples, ids = getImageAndLabels(path)
    train(face_samples, ids)
