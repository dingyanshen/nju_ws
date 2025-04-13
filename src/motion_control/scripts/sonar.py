#! /usr/bin/env python2.7
# -*- coding:utf-8 -*-

import rospy
from sensor_msgs.msg import Range

class Sonar:
    """超声波测距库"""

    def __init__(self):
        self.distSonar0 = 0.0
        self.distSonar1 = 0.0

        rospy.Subscriber("/sonar0", Range, self._sonar0_CB, queue_size=10)
        rospy.Subscriber("/sonar1", Range, self._sonar1_CB, queue_size=10)
        rospy.wait_for_message("/sonar0", Range)
        rospy.wait_for_message("/sonar1", Range)

    def _sonar0_CB(self, data):
        """超声波回调函数"""
        self.distSonar0 = data.range

    def _sonar1_CB(self, data):
        """超声波回调函数"""
        self.distSonar1 = data.range

    def getFrontDist(self):
        """获取前方距离"""
        dist = (self.distSonar0 + self.distSonar1) / 2
        return dist + 0.02  # 0.02是实测得到的固定误差

if __name__ == "__main__":
    rospy.init_node("sonar")

    SN = Sonar()

    while not rospy.is_shutdown():
        print("front dist: " + str(SN.getFrontDist()))
        print("---")
        rospy.sleep(0.5)

    rospy.signal_shutdown("")
    rospy.spin()