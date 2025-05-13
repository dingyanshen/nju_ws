
# Translation Vector:
#  [[-3.57393347] x车头
#  [-1.02586684] 没用
#  [25.00277962]] z相机前

import time
import cv2
import numpy
# from detect import detect
from pnp import pnp
import pyzbar.pyzbar as pyzbar
import numpy as np
def capture_callback(image):
    size = image.shape

    w = size[1] #宽度

    h = size[0] #高度
    if image is None:
        print("Failed to capture image")
        return
    print("Height: %d   Width: %d" % (h, w))


    h_ = 600
    w_ = int(w * (h_/h))
    # cv2.namedWindow("origin", cv2.WINDOW_NORMAL) 
    # cv2.resizeWindow("origin", w_, h_)
    # cv2.imshow("origin", image)
    # cv2.waitKey(0)  

    points = detect(image)
    rotation_matrix, translation_vector = pnp(points)
    print("Translation Vector:\n", translation_vector)
    print("Rotation Matrix:\n", rotation_matrix)
    
def detect(frame):
    decoded=pyzbar.decode(frame)
    for obj in decoded:
        #获取二维码在图像中的四个角点
        image_points = [
        [obj.polygon[0].x, obj.polygon[0].y],
        [obj.polygon[1].x, obj.polygon[1].y],
        [obj.polygon[2].x, obj.polygon[2].y],
        [obj.polygon[3].x, obj.polygon[3].y]
        ]
     # 转换为 NumPy 数组
    box = np.array(image_points, dtype=np.float32)

    # 计算质心
    cx, cy = np.mean(box, axis=0)

    # 按左上、右上、左下、右下排序
    sorted_box = sorted(box, key=lambda point: (point[1] < cy, point[0]))

    return sorted_box

def cam():
    camera=cv2.VideoCapture(0)
    (grabbed, img) = camera.read()
    capture_callback(img)


if __name__ == '__main__':
    cam()