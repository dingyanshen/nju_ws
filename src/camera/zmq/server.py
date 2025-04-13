# -*- coding:utf-8 -*-
import zmq
import easyocr

def find_province_number(results, match, num):
    for item in results:
        for char in item:
            if char in match:
                index = match.index(char)
                return num[index]
    return 0

def find_province_number_all(results, match, num):
    matched_numbers = []
    for item in results:
        for char in item:
            if char in match:
                index = match.index(char)
                matched_numbers.append(num[index])
    return matched_numbers

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")
reader = easyocr.Reader(['ch_sim', 'en'])
province_match = ['苏', '浙', '安', '徽', '河', '湖', '四', '川', '广', '东', '福', '建']
province_num = [1, 2, 3, 3, 4, 5, 6, 6, 7, 7, 8, 8]
print("Server is running...")

while True:
    message = socket.recv_string()

    try:
        results = reader.readtext(message)
        text_results = [result[1] for result in results]
        print(text_results)
        text_num = find_province_number(text_results, province_match, province_num)
        text_num_all = find_province_number_all(text_results, province_match, province_num)
        print(text_num_all)
        socket.send(str(text_num).encode())
        
    except Exception as e:
        socket.send(0)