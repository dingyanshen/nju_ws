#! /usr/bin/env python2.7
# -*- coding:utf-8 -*-

import rospy
import PyKDL
from geometry_msgs.msg import Pose, Twist
from math import sqrt, pow, pi, radians
from pid import PID
from lidar import Lidar

class BasicMove:
    """
    基本运动库
    实现了小车直线运动、自转运动、圆弧运动
    """

    def __init__(self, detailInfo=False, recordData=False):
        """
        detailInfo: 调用函数时是否展示详细信息
        recordData: 是否记录误差数据用于分析
        """
        self.LD = Lidar()  # 激光雷达测距类

        self.detailInfo = detailInfo  # 调用函数时是否展示详细信息
        self.recordData = recordData  # 是否记录误差数据用于分析

        self.file_path = "/home/eaibot/nju_ws/src/motion_control/data/"  # 保存误差数据的目标路径
        self.rateControl = rospy.Rate(500)  # 控制频率

        # 直线运动用到的PID控制器 通过控制线速度以控制横向距离
        self.PID_forward = PID(-3, -0.00, -0.00, setpoint=0.0)
        self.PID_forward.output_limits = (-0.3, 0.3)  # 限幅
        self.toleranceForward = 0.01  # 目标容忍范围 m

        # 直线运动用到的PID控制器 通过控制角速度以控制纵向距离
        self.PID_cross = PID(1, -0.0, -0.0, setpoint=0.0)
        self.PID_cross.output_limits = (-0.1, 0.1)  # 限幅

        # 自转运动用到的PID控制器
        self.PID_rotate = PID(-5, -0.0018, -0.0008, setpoint=0.0)
        self.PID_rotate.output_limits = (-0.5, 0.5)  # 限幅
        self.toleranceRotate = 0.01  # 目标容忍范围 rad

        # 订阅机器人位姿topic
        rospy.Subscriber("/robot_pose", Pose, self._robot_pose_CB, queue_size=10)
        rospy.wait_for_message("/robot_pose", Pose)

        # 速度指令发布
        self.pub_velCmd = rospy.Publisher("/cmd_vel", Twist, queue_size=10)

    def _robot_pose_CB(self, pose):
        """/robot_pose订阅回调函数"""
        self.poseCur = pose

    def _writeDataToFile(self, times, errors, file_name):
        """
        将数据写入目标文件中
        times: 时间数据
        errors: 误差数据
        file_name: 目标文件名
        """
        file = open(self.file_path + file_name, "w")

        for i in range(len(times)):
            data = times[i] + " " + errors[i] + "\n"
            file.write(data)

        file.close()
        print(file_name + " 已保存")

    def _getDistance(self, pose1, pose2):
        """
        获取两个Pose之间的直线距离
        pose1 pose2: 类型为geometry_msgs.msg.Pose
        """
        x1, x2 = pose1.position.x, pose2.position.x
        y1, y2 = pose1.position.y, pose2.position.y
        return sqrt(pow((x1 - x2), 2) + pow((y1 - y2), 2))

    def _getForwardErrorF(self, poseInit, targetDist, mode="normal"):
        """
        根据不同模式获取直线运动时横向距离存在的误差
        poseInit: 机器人初始位姿
        mode: 为normal 时targetDist是要移动的距离
        mode: 为lidar  时targetDist是与前方障碍物的目标距离
        """
        # 将目标位姿与当前位姿之间的距离作为误差
        if mode == "lidar":
            distFront = self.LD.getFrontDist()
            error = distFront - targetDist
        else:
            distance = self._getDistance(poseInit, self.poseCur)
            if targetDist > 0:
                error = targetDist - distance
            else:
                error = targetDist + distance

        return error

    def _getForwardErrorC(self, mode="normal"):
        """
        根据不同模式获取直线运动时纵向距离存在的误差
        mode: 为normal 时返回0
        mode: 为lidar  时返回当前位姿与要保持的纵向距离的误差
        """
        if mode == "lidar":
            # 当前方案不用PID_cross，返回0
            return 0
        else:
            return 0

    def _pubVelCmd(self, linear_x=0.0, angular_z=0.0):
        """
        发布速度指令
        linear_x: 直线运动速度
        angular_z: 自转运动速度
        """
        velCmd = Twist()
        velCmd.linear.x = linear_x
        velCmd.angular.z = angular_z

        self.pub_velCmd.publish(velCmd)

    def moveForward(self, targetDist, mode="normal"):
        """
        直线运动函数
        mode: 为normal 时targetDist是要移动的距离 接受正负值
        mode: 为lidar  时targetDist是与前方障碍物的目标距离
        """
        targetDist = float(targetDist)

        # 重置PID控制器
        self.PID_forward.reset()
        self.PID_cross.reset()

        if self.recordData:  # 记录error数据
            timeStart = rospy.Time.now()
            times, errors = [], []

        if self.detailInfo == True:  # 展示调用信息
            print("move forward " + str(targetDist) + "m with " + str(mode) + " mode")

        self.poseInit = self.poseCur  # 保存初始位姿
        error_f = self._getForwardErrorF(self.poseInit, targetDist, mode)
        error_c = self._getForwardErrorC(mode=mode)

        while abs(error_f) > self.toleranceForward and not rospy.is_shutdown():
            if self.recordData:  # 记录error数据
                time = rospy.Time.now() - timeStart
                times.append(str(time))
                errors.append(str(error_f))

            # 用PID控制器计算速度
            linear_x = self.PID_forward(error_f)
            angular_z = self.PID_cross(error_c) if mode == "lidar" else 0
            angular_z = angular_z if linear_x > 0 else -angular_z

            self._pubVelCmd(linear_x=linear_x, angular_z=angular_z)

            # 计算误差
            error_f = self._getForwardErrorF(self.poseInit, targetDist, mode)
            error_c = self._getForwardErrorC(mode=mode)

            self.rateControl.sleep()

        self.stop()

        if self.recordData:
            self._writeDataToFile(times, errors, "forward_" + str(targetDist) + ".txt")

    def _quatToRadians(self, quaternion_z, quaternion_w):
        """将四元数转换为弧度"""
        return PyKDL.Rotation.Quaternion(0, 0, quaternion_z, quaternion_w).GetRPY()[2]

    def _getRadians(self, pose):
        """将Pose数据转换为弧度"""
        return self._quatToRadians(pose.orientation.z, pose.orientation.w)

    def _getRotateError(self, radiansTarget, radiansCur, mode="normal"):
        """
        根据不同模式获取自转运动时存在的角度误差
        mode: 为normal 时
                radiansTarget: 目标角度 rad
                radiansCur: 当前角度 rad
        mode: 为lidar  时其他参数无效
        """
        if mode == "lidar":
            angleDiff = self.LD.getDiffAngle()
            angleDiff = radians(angleDiff)
        else:
            angleDiff = radiansTarget - radiansCur

            # 将弧度限制在[-pi, pi]
            while angleDiff > pi:
                angleDiff -= 2 * pi
            while angleDiff < -pi:
                angleDiff += 2 * pi

        return angleDiff

    def moveRotate(self, targetDegree, mode="normal"):
        """
        自转运动函数
        mode: 为normal 时targetDegree是目标角度 以开始导航时正对的角度为0°
        mode: 为lidar  时targetDegree是小车侧向与前方障碍物平行方向的角度差
        """
        radiansTarget = radians(float(targetDegree))

        # 重置PID控制器
        self.PID_rotate.reset()

        if self.recordData:  # 记录error数据
            timeStart = rospy.Time.now()
            times, errors = [], []

        if self.detailInfo == True:  # 展示调用信息
            print(
                "move rotate to " + str(targetDegree) + "° with " + str(mode) + " mode"
            )

        radiansCur = self._getRadians(self.poseCur)
        # 将目标位姿与当前位姿之间的差值作为误差
        error = self._getRotateError(radiansTarget, radiansCur, mode)

        while abs(error) > self.toleranceRotate and not rospy.is_shutdown():
            if self.recordData:  # 记录error数据
                time = rospy.Time.now() - timeStart
                times.append(str(time))
                errors.append(str(error))

            angular_z = self.PID_rotate(error)  # 用PID控制器计算速度
            self._pubVelCmd(angular_z=angular_z)

            radiansCur = self._getRadians(self.poseCur)
            error = self._getRotateError(radiansTarget, radiansCur, mode)

            self.rateControl.sleep()

        self.stop()

        if self.recordData:
            self._writeDataToFile(times, errors, "rotate_" + str(targetDegree) + ".txt")

    def moveArc(self, R, degree, direction, linear_x=0.2):
        """
        圆弧运动函数
        R: 圆周半径
        degree: 运动的圆弧对应的角度
        direction: 朝左/朝右偏转
        linear_x: 线速度
        """
        R, degree, linear_x = float(R), float(degree), float(linear_x)

        if direction not in ("LEFT", "RIGHT"):  # 确保direction传入正确
            print("direction must be LEFT or RIGHT")
            return

        if self.detailInfo == True:  # 展示调用信息
            print(
                "move arc with radius: "
                + str(R)
                + "m, degree: "
                + str(degree)
                + "°, direction: "
                + str(direction)
                + ", linear_x: "
                + str(linear_x)
            )

        # 计算运动时长
        theta = radians(degree)
        time = theta * R / abs(linear_x)

        # 计算角速度
        direction = 1 if direction == "LEFT" else -1
        angular_z = abs(linear_x) / R * direction

        timeInit = rospy.get_time()
        timeCur = timeInit
        while timeCur - timeInit < time and not rospy.is_shutdown():
            self._pubVelCmd(linear_x=linear_x, angular_z=angular_z)
            timeCur = rospy.get_time()
            rospy.sleep(0.01)

        self.stop()

    def stop(self):
        """停止运动函数"""
        self.pub_velCmd.publish(Twist())

if __name__ == "__main__":
    rospy.init_node("basic_move")

    BM = BasicMove(recordData=True)

    # 提示指令格式
    print(
        "请输入：\n前进：f targetDist mode\n自转：r targetDegree mode\n圆弧：a R degree direction linear_x"
    )

    while not rospy.is_shutdown():
        cmd = raw_input().split()
        cmd = [
            float(item) if item.replace(".", "", 1).isdigit() else item for item in cmd
        ]

        if cmd[0] == "f":
            BM.moveForward(cmd[1], cmd[2])
        elif cmd[0] == "r":
            BM.moveRotate(cmd[1], cmd[2])
        elif cmd[0] == "a":
            BM.moveArc(cmd[1], cmd[2], cmd[3], cmd[4])

    rospy.signal_shutdown("")
    rospy.spin()