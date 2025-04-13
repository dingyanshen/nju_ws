#! /usr/bin/env python2.7
# -*- coding:utf-8 -*-

import rospy
import numpy as np
from sensor_msgs.msg import LaserScan
from motion_control.srv import *

class Lidar:
    """激光雷达类"""

    def __init__(self):
        self.rangeFront = [425, 475]
        self.rangeRight = [805, 855]
        self.rangeLeft = [45, 95]
        self.rangeRightFront = [615, 665]
        self.rangeLeftFront = [235, 285]

        # 订阅激光雷达数据
        rospy.Subscriber("/scan", LaserScan, self._scan_CB)
        rospy.wait_for_message("/scan", LaserScan)

        # 提供获取距离的服务通信
        rospy.Service("getFrontDist", getFrontDist, self._getFrontDist_CB)
        rospy.Service("getRightDist", getRightDist, self._getRightDist_CB)
        rospy.Service("getLeftDist", getLeftDist, self._getLeftDist_CB)
        rospy.Service(
            "getRightFrontDist", getRightFrontDist, self._getRightFrontDist_CB
        )
        rospy.Service("getLeftFrontDist", getLeftFrontDist, self._getLeftFrontDist_CB)
        rospy.Service("getDiffAngle", getDiffAngle, self._getDiffAngle_CB)

        # 发布过滤后的scan数据，用于观测激光雷达扫描范围
        self.pub_scanFiltered = rospy.Publisher(
            "/scanFiltered", LaserScan, queue_size=10
        )

    def _scan_CB(self, scan):
        """激光雷达数据回调函数"""
        self.scanData = scan
        self.scanRanges = self.scanData.ranges  # 数组大小为ranges[910]

    def _getFrontDist_CB(self, req):
        """获取前方距离的服务通信回调函数"""
        resp = getFrontDistResponse(self.getFrontDist())
        return resp

    def _getRightDist_CB(self, req):
        """获取右方距离的服务通信回调函数"""
        resp = getRightDistResponse(self.getRightDist())
        return resp

    def _getLeftDist_CB(self, req):
        """获取左方距离的服务通信回调函数"""
        resp = getLeftDistResponse(self.getLeftDist())
        return resp

    def _getRightFrontDist_CB(self, req):
        """获取右前方距离的服务通信回调函数"""
        resp = getRightFrontDistResponse(self.getRightFrontDist())
        return resp

    def _getLeftFrontDist_CB(self, req):
        """获取右前方距离的服务通信回调函数"""
        resp = getLeftFrontDistResponse(self.getLeftFrontDist())
        return resp

    def _getDiffAngle_CB(self, req):
        """获取小车侧向与前方障碍物平行方向的角度差值的服务通信回调函数"""
        resp = getDiffAngleResponse(self.getDiffAngle())
        return resp

    def _getAverageDist(self, indexRange):
        """
        计算激光雷达数据index范围内去除0后的平均值
        indexRange: index范围
        """
        start = indexRange[0]
        end = indexRange[1]
        scanRanges = self.scanRanges[int(start) : int(end)]

        dist = False
        while dist == False and not rospy.is_shutdown():
            count_zero = 0
            for i in range(len(scanRanges)):
                if scanRanges[i] == 0:
                    count_zero += 1

            if len(scanRanges) == count_zero:
                continue
            else:
                dist = sum(scanRanges) / (len(scanRanges) - count_zero)

        return dist

    def getFrontDist(self):
        """获取前方距离"""
        return self._getAverageDist(self.rangeFront)

    def getRightDist(self):
        """获取右方距离"""
        return self._getAverageDist(self.rangeRight)

    def getLeftDist(self):
        """获取左方距离"""
        return self._getAverageDist(self.rangeLeft)

    def getRightFrontDist(self):
        """获取右前方距离"""
        return self._getAverageDist(self.rangeRightFront)

    def getLeftFrontDist(self):
        """获取左前方距离"""
        return self._getAverageDist(self.rangeLeftFront)

    def _leastSquares(self, x, y):
        """
        根据x和y用最小二乘法得到拟合直线的k和b
        x: x轴数据
        y: y轴数据
        """
        N = len(x)
        sum_x = sum(x)
        sum_y = sum(y)
        sum_x2 = sum(x**2)
        sum_xy = sum(x * y)
        A = np.mat([[N, sum_x], [sum_x, sum_x2]])
        b = np.array([sum_y, sum_xy])

        return np.linalg.solve(A, b)

    def getDiffAngle(self):
        """
        获取小车侧向与前方障碍物平行方向的角度差值
        向右偏转角度增大，向左偏转角度减小
        """
        scanRanges = self.scanRanges[425:475]

        y = np.array(scanRanges) * 100
        x = np.arange(len(scanRanges))

        filter = y != 0
        x = x[filter]
        y = y[filter]

        b, k = self._leastSquares(x, y)

        angle = np.degrees(np.arctan(k))
        return angle

    def pubScanFiltered(self, indexRange):
        """
        用indexRange过滤scan数据后发布，用于观测激光雷达扫描范围
        indexRange: list 其中两个元素分别为要观测数据范围的start、end
        """
        scanFiltered = self.scanData
        ranges = list(scanFiltered.ranges)

        start = indexRange[0]
        end = indexRange[1]
        for i in range(len(ranges)):
            ranges[i] = ranges[i] if i in range(start, end) else 0

        scanFiltered.ranges = tuple(ranges)
        self.pub_scanFiltered.publish(scanFiltered)


if __name__ == "__main__":
    rospy.init_node("lidar")

    LD = Lidar()
    while not rospy.is_shutdown():
        print("front dist: " + str(LD.getFrontDist()))
        print("right dist: " + str(LD.getRightDist()))
        print("left  dist: " + str(LD.getLeftDist()))
        print("diff angle: " + str(LD.getDiffAngle()))
        print("---")
        LD.pubScanFiltered(LD.rangeFront)
        rospy.sleep(0.5)

    rospy.signal_shutdown("")
    rospy.spin()