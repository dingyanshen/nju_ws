#! /usr/bin/env python2.7
# -*- coding:utf-8 -*-

import rospy
from lidar import Lidar

def recordDist(file_path):
    """
    根据用户输入的tableIndex记录邮件分拣台与侧方边界的距离
    file_path: 目标文件路径
    """
    # 打开文件
    file = open(file_path, "w+")

    # 提示指令格式
    print(
        "输入 q 退出\n输入 t + o(opposite) + index 记录正对着邮件盒的距离\n输入 t + b(between) + index 记录邮件盒正中间的距离："
    )

    LD = Lidar()
    while not rospy.is_shutdown():
        tableIndex = raw_input("请输入指令: ")

        if tableIndex == "q":
            print("退出程序......")
            break
        else:
            distFront = LD.getFrontDist()
            distMsg = tableIndex + " " + str(distFront)

            print("---")
            print(distMsg)
            print("---")
            file.write(distMsg + "\n")

    file.close()

if __name__ == "__main__":
    rospy.init_node("record_dist")

    # 指定文件路径
    file_path = "/home/eaibot/motion_control_ws/src/motion_control/config/dist.txt"
    print("file path is [" + file_path + "]")

    # 记录小车与前方边界的距离
    recordDist(file_path)

    rospy.signal_shutdown("")
    rospy.spin()