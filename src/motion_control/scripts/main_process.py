#! /usr/bin/env python2.7
# -*- coding:utf-8 -*-

import rospy
import actionlib
from geometry_msgs.msg import Pose, PoseWithCovarianceStamped, Point, Quaternion
from actionlib_msgs.msg import *
from camera.srv import PhotoshelfService, PhotoboxService
from dobot.srv import GraspService, ThrowService
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from basic_move import BasicMove

class MainController:
    def __init__(self,position_path):
        rospy.init_node('main_controller')
        self.BM = BasicMove(detailInfo=True)
        self.position = self.loadToDict(position_path, mode="pose")
        self.move_base_AS = actionlib.SimpleActionClient("move_base", MoveBaseAction)
        print("Connecting to move_base action server...")
        self.move_base_AS.wait_for_server(rospy.Duration(60))
        self.pub_initialpose = rospy.Publisher("/initialpose", PoseWithCovarianceStamped, queue_size=20)
        print("Waiting for photo_shelf_service...")
        rospy.wait_for_service('photo_shelf_service')
        print("Waiting for photo_box_service...")
        rospy.wait_for_service('photo_box_service')
        print("Waiting for dobot_grasp_service...")
        rospy.wait_for_service('dobot_grasp_service')
        print("Waiting for dobot_throw_service...")
        rospy.wait_for_service('dobot_throw_service')
        self.photo_shelf_proxy = rospy.ServiceProxy('photo_shelf_service', PhotoshelfService)
        self.photo_box_proxy = rospy.ServiceProxy('photo_box_service', PhotoboxService)
        self.grasp_proxy = rospy.ServiceProxy('dobot_grasp_service', GraspService)
        self.throw_proxy = rospy.ServiceProxy('dobot_throw_service', ThrowService)

        self.mail_table = [] # results.positions_z.positions_x
        self.mail_box = [] # box_id.result
        self.priority_provinces = [] # 省份优先级

    def loadToDict(self, file_path, mode): # 导入相关参数
        print("Loading " + str(mode) + "...")
        dictionary = dict()
        file = open(file_path, "r")
        for line in file:
            data = line.strip().split()
            if mode == "pose" and len(data) == 5:
                key, px, py, qz, qw = data
                px, py, qz, qw = float(px), float(py), float(qz), float(qw)
                pose = Pose(Point(px, py, 0.0), Quaternion(0.0, 0.0, qz, qw))
                dictionary[key] = pose
        file.close()
        print("Load " + str(mode) + " successfully!")
        return dictionary
    
    def welcome(self): # 欢迎界面
        welcome_msg = [
            "  _   _         _      _   _   ",
            " | \ | |       | |    | | | |  ",
            " |  \| |    _  | |    | | | |  ",
            " | |\  |   | |_| |    | |_| |  ",
            " |_| \_|    \___/      \___/   ",
            "                               ",
            "南    雍    智    运    未    来\n",
        ]
        for line in welcome_msg:
            print(line)

    def end(self): # 结束界面
        end_msg = [
            "  _   _         _      _   _   ",
            " | \ | |       | |    | | | |  ",
            " |  \| |    _  | |    | | | |  ",
            " | |\  |   | |_| |    | |_| |  ",
            " |_| \_|    \___/      \___/   ",
            "                               ",
            "任    务    顺    利    完    成\n",
        ]
        for line in end_msg:
            print(line)

    def calibratePose(self, poseKey): # 校准位姿
        print("Calibrating pose " + str(poseKey) + "...")
        originalPose = PoseWithCovarianceStamped()
        originalPose.header.frame_id = "map"
        originalPose.header.stamp = rospy.Time.now()
        originalPose.pose.pose = self.position[poseKey]
        originalPose.pose.covariance[0] = 0.01
        originalPose.pose.covariance[6 * 1 + 1] = 0.01
        originalPose.pose.covariance[6 * 5 + 5] = 0.01
        for _ in range(10):
            self.pub_initialpose.publish(originalPose)
            rospy.sleep(0.1)
        rospy.sleep(0.5)
        print("Calibrate pose " + str(poseKey) + " successfully!")

    def navigate_posekey(self, poseKey): # 导航到指定位置
        goal = MoveBaseGoal()
        goal.target_pose.header.frame_id = "map"
        goal.target_pose.header.stamp = rospy.Time.now()
        goal.target_pose.pose = self.position[poseKey]
        self.move_base_AS.send_goal(goal)
        while not self.move_base_AS.wait_for_result():
            pass

    def navigate_position(self, x,y): # 导航到指定坐标
        goal = MoveBaseGoal()
        goal.target_pose.header.frame_id = "map"
        goal.target_pose.header.stamp = rospy.Time.now()
        goal.target_pose.pose.position.x = x
        goal.target_pose.pose.position.y = y
        self.move_base_AS.send_goal(goal)
        while not self.move_base_AS.wait_for_result():
            pass

    def takeboxPic_RU(self): # 邮箱文字识别[右上]
        self.navigate_posekey("ARU2")
        print("ARU2 is arrived.")
        self.process_box("ARU2")

        self.navigate_posekey("ARU1")
        print("ARU1 is arrived.")
        self.process_box("ARU1")

    def takeboxPic_RD(self): # 邮箱文字识别[右下]
        self.navigate_posekey("ARD2")
        print("ARD2 is arrived.")
        self.process_box("ARD2")

        self.navigate_posekey("ARD1")
        print("ARD1 is arrived.")
        self.process_box("ARD1")
        
    def takeboxPic_LU(self): # 邮箱文字识别[左上]
        self.navigate_posekey("ALU1")
        print("ALU1 is arrived.")
        self.process_box("ALU1")

        self.navigate_posekey("ALU2")
        print("ALU2 is arrived.")
        self.process_box("ALU2")

    def takeboxPic_LD(self): # 邮箱文字识别[左下]
        self.navigate_posekey("ALD1")
        print("ALD1 is arrived.")
        self.process_box("ALD1")

        self.navigate_posekey("ALD2")
        print("ALD2 is arrived.")
        self.process_box("ALD2")
                
    def takeshelfPic_R(self): # 货架拍照[右侧]
        self.navigate_posekey("RP1")
        print("RP1 is arrived.")
        self.process_shelf(4)
        
        self.navigate_posekey("RP2")
        print("RP2 is arrived.")
        self.process_shelf(5)
        
        self.navigate_posekey("RP3")
        print("RP3 is arrived.")
        self.process_shelf(6)

    def takeshelfPic_L(self): # 货架拍照[左侧]
        self.navigate_posekey("LP3")
        print("LP3 is arrived.")
        self.process_shelf(1)

        self.navigate_posekey("LP2")
        print("LP2 is arrived.")
        self.process_shelf(2)
        
        self.navigate_posekey("LP1")
        print("LP1 is arrived.")
        self.process_shelf(3)

    def process_shelf(self, type): # 货架拍照服务
        try:
            response = self.photo_shelf_proxy(type)
            print(response)
            if type == 1 or type == 2 or type == 5 or type == 6:
                for i in range(4):
                    self.mail_table.append({
                        'results': response.results[i],
                        'positions_z': response.positions_z[i],
                        'positions_x': response.positions_x[i],
                    })
            elif type == 3:
                self.mail_table.append({
                    'results': response.results[0],
                    'positions_z': response.positions_z[0],
                    'positions_x': response.positions_x[0],
                })
                self.mail_table.append({
                    'results': response.results[2],
                    'positions_z': response.positions_z[2],
                    'positions_x': response.positions_x[2],
                })
            elif type == 4:
                self.mail_table.append({
                    'results': response.results[1],
                    'positions_z': response.positions_z[1],
                    'positions_x': response.positions_x[1],
                })
                self.mail_table.append({
                    'results': response.results[3],
                    'positions_z': response.positions_z[3],
                    'positions_x': response.positions_x[3],
                })
        except rospy.ServiceException as e:
            rospy.logerr("Photo service call failed: {e}")

    def process_box(self, box_id): # 邮箱拍照服务
        try:
            response = self.photo_box_proxy()
            print(response)
            self.mail_box.append({
                    'box_id': box_id,
                    'result': response
                })
            self.priority_provinces.append(response)
        except rospy.ServiceException as e:
            rospy.logerr("Photo service call failed: {e}")
    
    def grasp_mail(self, mail): # 抓取邮件
        try:
            self.navigate_posekey("CL" + str(mail['positions_x']))
            if mail[1] == 1: # 上层
                catch_type = [1, 1, 0, 0]
                response = self.grasp_proxy(*catch_type)
            elif mail[1] == 2: # 下层
                catch_type = [0, 1, 0, 0]
                response = self.grasp_proxy(*catch_type)
            else:
                rospy.logwarn("邮件位置不正确")
                return False
            if response.success:
                return True
            else:
                rospy.logwarn("抓取邮件失败")
                return False
        except rospy.ServiceException as e:
            rospy.logerr("抓取服务调用失败: {e}")
            return False
        
    def deliver_mails(self, mails): # 运送邮件
        try:
            for mail in mails:
                for box in self.mail_box:
                    if box['result'] == mail['results']:
                        self.navigate_posekey(box['box_id'])
                        break
                throw_type = [0, 0]
                response = self.throw_proxy(*throw_type)
                if not response.success:
                    rospy.logwarn("运送邮件失败")
                    return False
            return True
        except rospy.ServiceException as e:
            rospy.logerr("运送服务调用失败: {e}")
            return False
        
    def select_nearest_province(self): # 对mail_table按照priority_provinces重新排序
        priority_mails = [mail for mail in self.mail_table if mail['results'] in self.priority_provinces]
        other_mails = [mail for mail in self.mail_table if mail['results'] not in self.priority_provinces]
        sorted_mail_table = priority_mails + other_mails
        return sorted_mail_table
    
    def process_priority_mails(self): # 处理优先省份邮件
        grabbed_mails = []

        for mail in self.mail_table:
            if mail['results'] not in self.priority_provinces:
                break
            if self.grasp_mail(mail):
                grabbed_mails.append(mail)

                if len(grabbed_mails) >= 2:
                    self.deliver_mails(grabbed_mails)
                    self.mail_table = [mail for mail in self.mail_table if mail not in grabbed_mails]
                    grabbed_mails = []

        if grabbed_mails:
            self.deliver_mails(grabbed_mails)
            self.mail_table = [mail for mail in self.mail_table if mail not in grabbed_mails]
            grabbed_mails = []

    def process_non_priority_mails(self): # 处理非优先省份邮件
        grabbed_mails = []
        for mail in self.mail_table:
            for box in self.mail_box:
                    if box['result'] == mail['results']:
                        self.navigate_posekey(box['box_id'])
                        break
            if self.grasp_mail(mail):
                grabbed_mails.append(mail)

                if len(grabbed_mails) >= 2:
                    self.deliver_mails(grabbed_mails)
                    self.mail_table = [mail for mail in self.mail_table if mail not in grabbed_mails]
                    grabbed_mails = []

        if grabbed_mails:
            self.deliver_mails(grabbed_mails)
            self.mail_table = [mail for mail in self.mail_table if mail not in grabbed_mails]
            grabbed_mails = []

    def run(self):
        self.welcome() # 欢迎界面

        self.calibratePose("start") # 校准起始位姿

        self.takeboxPic_RU() # 邮箱拍照[右上]
        self.takeboxPic_RD() # 邮箱拍照[右下]
        self.takeshelfPic_R() # 货架拍照[右侧]
        self.mail_table = self.select_nearest_province() # 对mail_table按照priority_provinces重新排序
        self.process_priority_mails() # 处理右侧优先省份邮件

        self.priority_provinces = [] # 清空优先省份
        self.mail_table_temp = self.mail_table # 备份邮件列表
        self.mail_table = [] # 清空邮件列表

        self.takeboxPic_LD() # 邮箱拍照[左下]
        self.takeboxPic_LU() # 邮箱拍照[左上]
        self.takeshelfPic_L() # 货架拍照[左侧]
        self.mail_table = self.select_nearest_province() # 对mail_table按照priority_provinces重新排序
        self.process_priority_mails() # 处理左侧优先省份邮件

        self.mail_table = self.mail_table_temp + self.mail_table # 合并邮件列表
        
        self.process_non_priority_mails() # 处理非优先省份邮件

        self.end() # 结束界面

if __name__ == "__main__":
    position_path = "/home/eaibot/nju_ws/src/motion_control/config/position.txt"
    controller = MainController(position_path)
    controller.run()