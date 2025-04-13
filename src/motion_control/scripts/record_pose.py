#! /usr/bin/env python2.7
# -*- coding:utf-8 -*-

import rospy
from geometry_msgs.msg import Pose

def isCommandValid(command):
    """
    检查指令字符串是否合法
    command: 待检查的命令字符串
    """

    if (
        len(command) == 3
        and command[0] == "t"
        and command[1] in ("o", "b")
        and command[2].isdigit()
    ):
        return True

    if (
        len(command) == 3
        and command[0] == "b"
        and command[1].isdigit()
        and command[2] in ("f", "b", "l", "r")
    ):
        return True

    return False

def recordPose(file_path):
    """
    根据用户输入的指令记录位姿信息目标文件
    file_path: 目标文件路径
    """

    file = open(file_path, "w+")  # 打开文件
    file.write("start 0 0 0 1\n")  # 添加出发点位姿

    while not rospy.is_shutdown():
        instruction = raw_input("请输入指令: ")

        if instruction == "q":
            print("退出程序......")
            break
        elif isCommandValid(instruction):
            curPose = rospy.wait_for_message("/robot_pose", Pose)
            poseMsg = (
                instruction
                + " "
                + str(curPose.position.x)
                + " "
                + str(curPose.position.y)
                + " "
                + str(curPose.orientation.z)
                + " "
                + str(curPose.orientation.w)
            )
            print("---")
            print(poseMsg)
            print("---")
            file.write(poseMsg + "\n")
        else:
            print("无效指令")

    file.close()

if __name__ == "__main__":
    rospy.init_node("record_pose")

    # 指定文件路径
    file_path = "/home/eaibot/motion_control_ws/src/motion_control/config/pose.txt"
    print("file path is [" + file_path + "]")

    # 等待/robot_pose话题启动
    rospy.wait_for_message("/robot_pose", Pose)

    # 提示指令格式
    print(
        "指令格式:\nq(quit)\nb(box) + num + f(front)/b(back)/l(left)/r(right)\nt(table) + o(opposite)/b(between) + num"
    )

    # 记录邮件盒和邮件分拣台的位姿
    recordPose(file_path)

    rospy.signal_shutdown("")
    rospy.spin()