#! /usr/bin/env python2.7
# -*- coding:utf-8 -*-
import time
import rospy
from camera.srv import PhotoshelfService, PhotoshelfServiceResponse, PhotoshelfServiceRequest
from camera.srv import PhotoboxService, PhotoboxServiceResponse, PhotoboxServiceRequest
import cv2
import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://192.168.31.200:5555")

class PhotoServiceNode:
    def __init__(self):
        rospy.init_node('photo_service')
        self.service_shelf = rospy.Service('photo_shelf_service', PhotoshelfService, self.handle_shelf_photo)
        self.service_box = rospy.Service('photo_box_service', PhotoboxService, self.handle_box_photo)
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            rospy.logerr("Camera initialization failed!")
            rospy.signal_shutdown("Camera initialization failed!")

    def handle_box_photo(self, req):
        # self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        # self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 960)
        for _ in range(10):
            self.cap.grab()
        ret, frame = self.cap.read()
        if not ret:
            rospy.logwarn("read camera failed")
            return PhotoboxServiceResponse(0)
        image_name = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())
        image_path = "/home/eaibot/nju_ws/src/camera/img/box_image_{}.jpg".format(image_name)
        cv2.imwrite(image_path, frame, [cv2.IMWRITE_PNG_COMPRESSION, 0]) 
        socket.send_string(image_path)
        response = socket.recv()
        num_province = ['无效', '江苏', '浙江', '安徽', '河南', '湖南', '四川', '广东', '福建']
        print(num_province[int(response)])
        return PhotoboxServiceResponse(int(response))
    
    def handle_shelf_photo(self, req):
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 960)
        ret, frame = self.cap.read()
        if not ret:
            rospy.logwarn("read camera failed")
            return PhotoshelfServiceResponse([], [], [], [])

        decoded = pyzbar.decode(frame)
        province_name = decoded
        province_names = []
        positions_x = []
        positions_y = []
        codes = []
        '''
        for obj in decoded:
            # 解析省份名称（假设二维码内容是省份字符串）
            province_name = obj.data.decode('utf-8')
            province_names.append(province_name)

            # 获取二维码相对于图像的坐标
            x = obj.rect.left + obj.rect.width // 2
            y = obj.rect.top + obj.rect.height // 2
            positions_x.append(x)
            positions_y.append(y)

            # 假设省份名称与代号的映射关系
            code_map = {
                "江苏": "U",
                "浙江": "Z",
                "广东": "G",
                "山东": "S",
                # 添加更多省份映射
            }
            code = code_map.get(province_name, "未知代号")
            codes.append(code)

            rospy.loginfo(f"识别到省份: {province_name}, 坐标: ({x}, {y}), 代号: {code}")
        '''

        # 返回响应
        return PhotoshelfServiceResponse(province_names, positions_x, positions_y, codes)

    # def __del__(self):
    #     # 释放摄像头资源
    #     if self.cap.isOpened():
    #         self.cap.release()

if __name__ == "__main__":
    node = PhotoServiceNode()
    rospy.spin()