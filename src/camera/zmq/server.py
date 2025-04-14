# -*- coding:utf-8 -*-
import cv2
import zmq
import easyocr

def qrcode_barcodes():
    img = cv2.imread(message)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    barcodes, points = model.detectAndDecode(gray)
    text_num = find_province_number(barcodes, province_match, province_num)
    socket.send(str(text_num).encode())

def qrcode_points():
    img = cv2.imread(message)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    barcodes, points = model.detectAndDecode(gray)
    socket.send(str(points).encode())

def shelf():
    img = cv2.imread(message)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    results = reader.readtext(gray)
    text_results = [result[1] for result in results]
    print(text_results)
    text_num = find_province_number_double(text_results, province_match_double)
    socket.send(str(text_num).encode())

def box():
    img = cv2.imread(message)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    results = reader.readtext(gray)
    text_results = [result[1] for result in results]
    print(text_results)
    text_num = find_province_number(text_results, province_match, province_num)
    socket.send(str(text_num).encode())

def find_province_number(results, match, num):
    for item in results:
        for char in item:
            if char in match:
                index = match.index(char)
                return num[index]
    return 0

def find_province_number_double(results, match_double):
    for item in results:
        for province in match_double:
            if province in item:
                return match_double.index(province) + 1
    return 0
            
if __name__ == "__main__":
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")
    depro = '/home/eaibot/nju_ws/src/camera/config/detect.prototxt'
    decaf = '/home/eaibot/nju_ws/src/camera/config/detect.caffemodel'
    srpro = '/home/eaibot/nju_ws/src/camera/config/sr.prototxt'
    srcaf = '/home/eaibot/nju_ws/src/camera/config/sr.caffemodel'
    model = cv2.wechat_qrcode_WeChatQRCode(depro, decaf, srpro, srcaf)
    reader = easyocr.Reader(['ch_sim', 'en'])
    province_match = ['苏', '浙', '安', '徽', '河', '湖', '四', '川', '广', '东', '福', '建']
    province_match_double =['江苏', '浙江', '安徽', '河南', '湖南', '四川', '广东', '福建']
    province_num = [1, 2, 3, 3, 4, 5, 6, 6, 7, 7, 8, 8]
    print("Server is running...")

    while True:
        message = socket.recv_string()

        try:
            if message.startswith("/home/eaibot/nju_ws/src/camera/img/qrcode_barcodes_image"):
                qrcode_barcodes()
            elif message.startswith("/home/eaibot/nju_ws/src/camera/img/qrcode_points_image"):
                qrcode_points()
            elif message.startswith("/home/eaibot/nju_ws/src/camera/img/shelf_image"):
                shelf()
            elif message.startswith("/home/eaibot/nju_ws/src/camera/img/box_image"):
                box()

        except Exception as e:
            socket.send(b"0")