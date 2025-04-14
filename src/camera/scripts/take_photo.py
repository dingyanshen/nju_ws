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
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
        for _ in range(10):
            self.cap.grab()
        ret, frame = self.cap.read()
        frame = frame[160:240, 0:320]
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
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
        for _ in range(10):
            self.cap.grab()
        ret, frame = self.cap.read()
        ret, frame = self.cap.read()
        if not ret:
            rospy.logwarn("read camera failed")
            return PhotoshelfServiceResponse([], [], [], [])
        image_name = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())
        image_path = "/home/eaibot/nju_ws/src/camera/img/shelf_image_{}.jpg".format(image_name)
        cv2.imwrite(image_path, frame, [cv2.IMWRITE_PNG_COMPRESSION, 0]) 
        socket.send_string(image_path)
        response = socket.recv()
        num_province = ['无效', '江苏', '浙江', '安徽', '河南', '湖南', '四川', '广东', '福建']
        print(num_province[int(response)])
        return PhotoboxServiceResponse(int(response))
    
    # def handle_shelf_photo(self, req):
    #     self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    #     self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 960)
    #     for _ in range(10):
    #         self.cap.grab()
    #     ret, frame = self.cap.read()
    #     ret, frame = self.cap.read()
    #     if not ret:
    #         rospy.logwarn("read camera failed")
    #         return PhotoshelfServiceResponse([], [], [], [])
    #     image_name = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())
    #     image_path = "/home/eaibot/nju_ws/src/camera/img/shelf_image_{}.jpg".format(image_name)
    #     cv2.imwrite(image_path, frame, [cv2.IMWRITE_PNG_COMPRESSION, 0]) 
    #     socket.send_string(image_path)
    #     response = socket.recv()
    #     # num_province = ['无效', '江苏', '浙江', '安徽', '河南', '湖南', '四川', '广东', '福建']
    #     # print(num_province[int(response)])
    #     # return PhotoboxServiceResponse(int(response))
    #     # return PhotoshelfServiceResponse(province_names, positions_x, positions_y, codes)

    # def __del__(self):
    #     # 释放摄像头资源
    #     if self.cap.isOpened():
    #         self.cap.release()

if __name__ == "__main__":
    node = PhotoServiceNode()
    rospy.spin()