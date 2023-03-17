import numpy as np
import cv2

# 级联分类器
face_cascade = cv2.CascadeClassifier('D:/opencv/sources/data/haarcascades/haarcascade_frontalface_alt2.xml')

# 调用摄像头
cap = cv2.VideoCapture(0)

while 1:
    # 按帧读取视频，它返回一个布尔值和一个视频帧1,2,3,4。布尔值表示是否读取成功，视频帧是一个三维矩阵，表示图像的BGR形式
    ret, img = cap.read()
    # 将图像水平翻转
    img = cv2.flip(img, 1)
    # 颜色空间转换，将图像转为灰度图片
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 检测图片中不同大小的对象，并返回矩形的列表；后面的参数分别为：scalefactor（图片缩小比例）1-1.5 ；minneighbors（矩形邻居数）
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        # 画矩形框，参数分别为左上角坐标、右下角坐标、颜色、粗细（注意：y轴正方向是向下的）
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        # 从图像中返回裁剪后的人脸。
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]
        # 打印矩形框中心位置坐标
        print(int(x + w / 2), int(y + h / 2))

    cv2.imshow('img', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:  # press 'ESC' to quit
        break
# 释放摄像头
cap.release()
# 释放所有资源
cv2.destroyAllWindows()
