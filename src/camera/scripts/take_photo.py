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
        if not ret:
            rospy.logwarn("read camera failed")
            return PhotoshelfServiceResponse([], [], [])
        image_name = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())
        image_path_shelf_1 = "/home/eaibot/nju_ws/src/camera/img/shelf_image_1_{}.jpg".format(image_name)
        image_path_shelf_2 = "/home/eaibot/nju_ws/src/camera/img/shelf_image_2_{}.jpg".format(image_name)
        image_path_shelf_3 = "/home/eaibot/nju_ws/src/camera/img/shelf_image_3_{}.jpg".format(image_name)
        image_path_shelf_4 = "/home/eaibot/nju_ws/src/camera/img/shelf_image_4_{}.jpg".format(image_name)
        image_path_qrcode_barcodes_1 = "/home/eaibot/nju_ws/src/camera/img/qrcode_barcodes_image_1_{}.jpg".format(image_name)
        image_path_qrcode_barcodes_2 = "/home/eaibot/nju_ws/src/camera/img/qrcode_barcodes_image_2_{}.jpg".format(image_name)
        image_path_qrcode_barcodes_3 = "/home/eaibot/nju_ws/src/camera/img/qrcode_barcodes_image_3_{}.jpg".format(image_name)
        image_path_qrcode_barcodes_4 = "/home/eaibot/nju_ws/src/camera/img/qrcode_barcodes_image_4_{}.jpg".format(image_name)
        image_path_qrcode_points_1 = "/home/eaibot/nju_ws/src/camera/img/qrcode_points_image_1_{}.jpg".format(image_name)
        image_path_qrcode_points_2 = "/home/eaibot/nju_ws/src/camera/img/qrcode_points_image_2_{}.jpg".format(image_name)
        image_path_qrcode_points_3 = "/home/eaibot/nju_ws/src/camera/img/qrcode_points_image_3_{}.jpg".format(image_name)
        image_path_qrcode_points_4 = "/home/eaibot/nju_ws/src/camera/img/qrcode_points_image_4_{}.jpg".format(image_name)
        frame1 = frame[0:480, 0:640]
        frame2 = frame[0:480, 640:1280]
        frame3 = frame[480:960, 0:640]
        frame4 = frame[480:960, 640:1280]
        cv2.imwrite(image_path_shelf_1, frame1, [cv2.IMWRITE_PNG_COMPRESSION, 0])
        cv2.imwrite(image_path_shelf_2, frame2, [cv2.IMWRITE_PNG_COMPRESSION, 0])
        cv2.imwrite(image_path_shelf_3, frame3, [cv2.IMWRITE_PNG_COMPRESSION, 0])
        cv2.imwrite(image_path_shelf_4, frame4, [cv2.IMWRITE_PNG_COMPRESSION, 0])

        socket.send_string(image_path_shelf_1)
        response_1 = socket.recv()
        socket.send_string(image_path_shelf_2)
        response_2 = socket.recv()
        socket.send_string(image_path_shelf_3)
        response_3 = socket.recv()
        socket.send_string(image_path_shelf_4)
        response_4 = socket.recv()
        num_province = ['无效', '江苏', '浙江', '安徽', '河南', '湖南', '四川', '广东', '福建']
        print(num_province[int(response_1)])
        print(num_province[int(response_2)])
        print(num_province[int(response_3)])
        print(num_province[int(response_4)])
        return PhotoshelfServiceResponse([int(response_1), int(response_2), int(response_3), int(response_4)], [1, 1, 2, 2], [1, 2, 1, 2])

if __name__ == "__main__":
    node = PhotoServiceNode()
    rospy.spin()