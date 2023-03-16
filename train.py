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
    对所有照片进行分析处理
    :return: 特征数组，标签
    """

    # 人脸数组列表和标签列表
    faceSamples = []
    ids = []

    path = "./facemessage"
    imagePaths = [os.path.join(path, f) for f in listdir(path)]

    # 遍历列表中的图片
    for imagePaths in imagePaths:

        pil_img = Image.open(imagePaths).convert('L')
        img_numpy = np.array(pil_img, 'uint8')

        face_detector = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
        face = face_detector.detectMultiScale(img_numpy)

        id = int(os.path.split(imagePaths)[1].split('.')[0])

        #  x, y, w, h给出了人脸的位置信息
        for x, y, w, h in face:
            ids.append(id)
            faceSamples.append(img_numpy[y:y + h, x:x + w])
    # 打印id和面部特征
    # print('id:', id)
    # print('fs:', faceSamples)
    return faceSamples, ids


if __name__ == '__main__':

    faces, ids = getImageAndLabels()
    # 加载识别器
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    # 人脸数组与id绑定，开始训练数据
    recognizer.train(faces, np.array(ids))
    # 保存文件
    recognizer.write('trainer/trainer.yml')
