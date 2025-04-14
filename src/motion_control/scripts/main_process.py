#! /usr/bin/env python2.7
# -*- coding:utf-8 -*-

import rospy
import actionlib
from math import sqrt, pow
from geometry_msgs.msg import Pose, PoseWithCovarianceStamped, Point, Quaternion
from actionlib_msgs.msg import *
from camera.srv import PhotoshelfService, PhotoboxService
from dobot.srv import GraspService, ThrowService
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from basic_move import BasicMove

class MainController:
    def __init__(self,position_path):
        rospy.init_node('main_controller')
        self.BM = BasicMove(detailInfo=True) # 基本运动库
        self.position = self.loadToDict(position_path, mode="pose")

        # 创建move_base Action Server并等待其启动
        self.move_base_AS = actionlib.SimpleActionClient("move_base", MoveBaseAction)
        print("Connecting to move_base action server...")
        self.move_base_AS.wait_for_server(rospy.Duration(60))
        
        # 校准位姿话题发布方
        self.pub_initialpose = rospy.Publisher("/initialpose", PoseWithCovarianceStamped, queue_size=20)

        # 初始化服务代理
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

        # 存储邮件信息的表，显示目前所有被拍到的并未被投掷的二维码信息
        self.mail_table = []
        self.mail_box = []
        self.priority_provinces = []

    def loadToDict(self, file_path, mode):
        """
        将数据加载到dict中
        file_path: 目标文件路径
        mode: 模式 pose/distance可选
        """
        print("Loading " + str(mode) + "...")
        dictionary = dict()

        file = open(file_path, "r")
        for line in file:
            data = line.strip().split()
            if mode == "pose" and len(data) == 5:
                # pz = qx = qy = 0
                key, px, py, qz, qw = data
                px, py, qz, qw = float(px), float(py), float(qz), float(qw)
                pose = Pose(Point(px, py, 0.0), Quaternion(0.0, 0.0, qz, qw))
                dictionary[key] = pose

            elif mode == "distance" and len(data) == 2:
                key, distance = data
                distance = float(distance)
                dictionary[key] = distance

        file.close()
        print("Load " + str(mode) + " successfully!")
        return dictionary
    
    def welcome(self):
        """
        欢迎界面
        """
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

    def calibratePose(self, poseKey):
        """
        校准位姿
        poseKey: pose dict中的key
        """

        if poseKey == "b0b":
            return

        print("Calibrating pose " + str(poseKey) + "...")

        originalPose = PoseWithCovarianceStamped()
        originalPose.header.frame_id = "map"
        originalPose.header.stamp = rospy.Time.now()
        if poseKey == "curPose":
            originalPose.pose.pose = rospy.wait_for_message("/robot_pose", Pose)
        else:
            originalPose.pose.pose = self.position[poseKey]

        originalPose.pose.covariance[0] = 0.25
        originalPose.pose.covariance[6 * 1 + 1] = 0.25
        originalPose.pose.covariance[6 * 5 + 5] = 0.06853891945200942

        for _ in range(10):
            self.pub_initialpose.publish(originalPose)
            rospy.sleep(0.05)
        rospy.sleep(0.5)  # 等待校准完成

        print("Calibrate pose " + str(poseKey) + " successfully!")

    def navigate_posekey(self, poseKey):
        """
        向move_base action发送导航目标点，到达目标点后退出
        """
        goal = MoveBaseGoal()
        goal.target_pose.header.frame_id = "map"
        goal.target_pose.header.stamp = rospy.Time.now()
        goal.target_pose.pose = self.position[poseKey]

        self.move_base_AS.send_goal(goal)
        while not self.move_base_AS.wait_for_result():
            pass

    def navigate_position(self, x,y):
        """
        向move_base action发送导航目标点，到达目标点后退出
        """
        goal = MoveBaseGoal()
        goal.target_pose.header.frame_id = "map"
        goal.target_pose.header.stamp = rospy.Time.now()
        goal.target_pose.pose.position.x = x
        goal.target_pose.pose.position.y = y
        ###pose中的其他补充变量

        self.move_base_AS.send_goal(goal)
        while not self.move_base_AS.wait_for_result():
            pass

    def takeboxPic_RU(self):
        """
        邮箱文字识别[右上]
        """
        self.navigate_posekey("ARU2")#到达目标点位
        print("ARU2 is arrived.")
        self.process_box("ARU2")#拍照

        self.navigate_posekey("ARU1")#到达目标点位
        print("ARU1 is arrived.")
        self.process_box("ARU1")#拍照

    def takeboxPic_RD(self):
        """
        邮箱文字识别[右下]
        """
        self.navigate_posekey("ARD2")#到达目标点位
        print("ARD2 is arrived.")
        self.process_box("ARD2")#拍照
        rospy.sleep(0.5)

        self.navigate_posekey("ARD1")#到达目标点位
        print("ARD1 is arrived.")
        self.process_box("ARD1")#拍照
        rospy.sleep(0.5)
        
    def takeboxPic_LU(self):
        """
        邮箱文字识别[左上]
        """
        self.navigate_posekey("ALU1")#到达目标点位
        print("ALU1 is arrived.")
        self.process_box("ALU1")#拍照
        rospy.sleep(0.5)

        self.navigate_posekey("ALU2")#到达目标点位
        print("ALU2 is arrived.")
        self.process_box("ALU2")#拍照
        rospy.sleep(0.5)

    def takeboxPic_LD(self):
        """
        邮箱文字识别[左下]
        """
        self.navigate_posekey("ALD1")#到达目标点位
        print("ALD1 is arrived.")
        self.process_box("ALD1")#拍照
        rospy.sleep(0.5)

        self.navigate_posekey("ALD2")#到达目标点位
        print("ALD2 is arrived.")
        self.process_box("ALD2")#拍照
        rospy.sleep(0.5)
                
    def takeshelfPic_R(self):
        """
        货架拍照[右侧]
        """
        self.navigate_posekey("RP1")#到达目标点位
        print("RP1 is arrived.")
        self.process_shelf(4)#拍照
        rospy.sleep(0.5)
        
        self.navigate_posekey("RP2")#到达目标点位
        print("RP2 is arrived.")
        self.process_shelf(5)#拍照
        rospy.sleep(0.5)
        
        self.navigate_posekey("RP3")#到达目标点位
        print("RP3 is arrived.")
        self.process_shelf(6)#拍照
        rospy.sleep(0.5)

    def takeshelfPic_L(self):
        """
        货架拍照[左侧]
        """
        self.navigate_posekey("LP3")#到达目标点位
        print("LP3 is arrived.")
        self.process_shelf(1)#拍照
        rospy.sleep(0.5)
        
        self.navigate_posekey("LP2")#到达目标点位
        print("LP2 is arrived.")
        self.process_shelf(2)#拍照
        rospy.sleep(0.5)
        
        self.navigate_posekey("LP1")#到达目标点位
        print("LP1 is arrived.")
        self.process_shelf(3)#拍照
        rospy.sleep(0.5)

    def process_shelf(self, type):
        # 调用拍照服务 货架
        try:
            response = self.photo_shelf_proxy(type)
            print(response)
            # self.mail_table.append({
            #     'province': response[0],
            #     'position_z': response[1],
            #     'position_x': response[2],
            #     })
        except rospy.ServiceException as e:
            rospy.logerr("Photo service call failed: {e}")

    def process_box(self, box_id):
        # 调用拍照服务 邮箱
        try:
            response = self.photo_box_proxy()
            print(response)
            # self.mail_box.append({
            #         'box_id': box_id,
            #         'province': response
            #     })
            # self.priority_provinces.append(response)
        except rospy.ServiceException as e:
            rospy.logerr("Photo service call failed: {e}")
    
    def select_nearest_province(self):
        """
        直接对self,mail_table重新排序
        要求把当前区域的省份，如：江苏、安徽、河南、浙江排在前面
        """
        # 分割为优先和非优先邮件
        priority_mails = [mail for mail in self.mail_table if mail['province'] in self.priority_provinces]
        other_mails = [mail for mail in self.mail_table if mail['province'] not in self.priority_provinces]

        # 合并列表（优先省份在前）
        sorted_mail_table = priority_mails + other_mails

        return sorted_mail_table
    
    def process_priority_mails(self):
        # 临时存放已抓取的邮件
        grabbed_mails = []
        
        # 遍历处理每个邮件
        for mail in self.mail_table:
            # 如果遇到非优先省份，停止处理
            if mail['province'] not in self.priority_provinces:
                rospy.loginfo("遇到非优先省份 {mail['province']}，停止处理")
                break
                
            # 导航到当前邮件位置
            rospy.loginfo("导航至 {mail['province']} (x:{mail['x']}, y:{mail['y']})")
            if not self.navigate_position(mail['code']):
                rospy.logwarn("导航至 {mail['province']} 失败，跳过该邮件")
                continue
                
            # 抓取当前邮件
            rospy.loginfo("开始抓取 {mail['province']} 的邮件")
            if self.grasp_mail(mail):
                grabbed_mails.append(mail)
                rospy.loginfo("成功抓取 {mail['province']} 的邮件")
                
                # 每抓取两个邮件执行运送
                if len(grabbed_mails) >= 2:
                    self.deliver_mails(grabbed_mails)
                    self.mail_table = [
                        mail for mail in self.mail_table if mail not in grabbed_mails
                    ]
                    grabbed_mails = []  # 清空已抓取邮件列表
        
        # 处理最后剩余的邮件（如果数量只剩1个）
        if grabbed_mails:
            self.deliver_mails(grabbed_mails)
            self.mail_table = [
                        mail for mail in self.mail_table if mail not in grabbed_mails
                    ]
            grabbed_mails = []  # 清空已抓取邮件列表

    def grasp_mail(self, mail):
        """
        抓取邮件
        mail: 邮件信息字典，包含省份、坐标、代号等信息
        """
        try:
            self.navigate_posekey(mail['code'])
            response = self.grasp_proxy(mail)
            if response.success:
                return True
            else:
                rospy.logwarn("抓取邮件失败")
                return False
        except rospy.ServiceException as e:
            rospy.logerr("抓取服务调用失败: {e}")
            return False
        
    def deliver_mails(self, mails):
        """
        运送邮件
        mails: 邮件列表，包含多个邮件信息字典
        """
        try:
            for mail in mails:
                # 执行运送操作
                for box in self.mail_box:
                    if box['province'] == mail['province']:
                        self.navigate_posekey(box['posekey'])
                        break
                response = self.throw_proxy()
                if not response.success:
                    rospy.logwarn("运送邮件失败")
                    return False
            return True
        except rospy.ServiceException as e:
            rospy.logerr("运送服务调用失败: {e}")
            return False
        
    def process_non_priority_mails(self):
        """
        处理优先省份邮件：
        1. 每次抓取两个邮件
        2. 执行运送操作
        3. 直到遇到非优先省份
        """
        # 临时存放已抓取的邮件
        grabbed_mails = []
        
        # 遍历处理每个邮件
        for mail in self.mail_table:
                
            # 导航到当前邮件位置
            rospy.loginfo("导航至 {mail['province']} (x:{mail['x']}, y:{mail['y']})")
            for box in self.mail_box:
                    if box['province'] == mail['province']:
                        self.navigate_posekey(box['posekey'])
                        break
            '''
            这里加上再次识别二维码，获得当前邮件相对于机械臂baselink的坐标，机械臂根据坐标抓取邮件
            '''
            # 抓取当前邮件
            rospy.loginfo("开始抓取 {mail['province']} 的邮件")
            if self.grasp_mail('传入邮件相对于机械臂baselink的坐标'):
                grabbed_mails.append(mail)
                rospy.loginfo("成功抓取 {mail['province']} 的邮件")
                
                # 每抓取两个邮件执行运送
                if len(grabbed_mails) >= 2:
                    self.deliver_mails(grabbed_mails)
                    self.mail_table = [
                        mail for mail in self.mail_table if mail not in grabbed_mails
                    ]
                    grabbed_mails = []  # 清空已抓取邮件列表
        
        # 处理最后剩余的邮件（如果数量只剩1个）
        if grabbed_mails:
            self.deliver_mails(grabbed_mails)
            self.mail_table = [
                        mail for mail in self.mail_table if mail not in grabbed_mails
                    ]
            grabbed_mails = []  # 清空已抓取邮件列表

    # def run(self):
    #     ## 主程序
    #     self.welcome() # 欢迎界面
    #     self.calibratePose("start") # 校准位姿
    #     self.takeboxPic_LD() # 邮箱拍照[左下]
    #     print("邮箱拍照[左下]")
    #     self.takeboxPic_LU() # 邮箱拍照[左上]
    #     print("邮箱拍照[左上]")
    #     self.takeboxPic_RU() # 邮箱拍照[右上]
    #     print("邮箱拍照[右上]")
    #     self.takeboxPic_RD() # 邮箱拍照[右下]
    #     print("邮箱拍照[右下]")
    #     self.navigate_posekey("start") # 返回起始位置
    #     print("返回起始位置")

    # def run(self):
    #     ## 主程序
    #     self.welcome() # 欢迎界面
    #     self.calibratePose("start") # 校准位姿
    #     # print('等待程序初始化完成...')
    #     # rospy.sleep(10) #预留给机械臂复位
    #     # print('还剩20秒...')
    #     # rospy.sleep(5)
    #     # print('还剩15秒...')
    #     # rospy.sleep(5)
    #     # print('还剩10秒...')
    #     # rospy.sleep(5)
    #     # print('还剩5秒...')
    #     # rospy.sleep(5)
    #     # print('开始运行...')
    #     self.BM.moveArc(0.5, 80, "LEFT", 0.3) # 左转90度 半径0.5米
    #     print("左转90度 半径0.5米")
    #     self.BM.moveForward(0.3, mode="normal") # 前进0.3米
    #     print("前进0.3米")

    #     self.navigate_posekey("LD1") # 河南
    #     print("河南")
    #     mail = [1, 0]
    #     response = self.throw_proxy(*mail)
    #     if response.success:
    #         print("投掷成功")
    #     else:
    #         print("投掷失败")

    #     self.navigate_posekey("LD2") # 湖南
    #     print("湖南")
    #     mail = [0, 0]
    #     response = self.throw_proxy(*mail)
    #     if response.success:
    #         print("投掷成功")
    #     else:
    #         print("投掷失败")
        
    #     self.BM.moveForward(0.25, mode="normal") # 前进0.25米
    #     print("前进0.25米")

    #     self.navigate_posekey("LP3") # 货架
    #     print("货架")
    #     mail = [1, 0, 100, 0]
    #     response = self.grasp_proxy(*mail)
    #     if response.success:
    #         print("抓取成功")
    #     else:
    #         print("抓取失败")
    #     mail = [0, 1, 100, 0]
    #     response = self.grasp_proxy(*mail)
    #     if response.success:
    #         print("抓取成功")
    #     else:
    #         print("抓取失败")

    #     self.BM.moveForward(1.0, mode="normal") # 前进1.0米
    #     print("前进1.0米")

    #     self.navigate_posekey("LU1") # 四川
    #     print("四川")
    #     mail = [1, 0]
    #     response = self.throw_proxy(*mail)
    #     if response.success:
    #         print("投掷成功")
    #     else:
    #         print("投掷失败")

    #     self.navigate_posekey("LU2") # 浙江
    #     print("浙江")
    #     mail = [0, 0]
    #     response = self.throw_proxy(*mail)
    #     if response.success:
    #         print("投掷成功")
    #     else:
    #         print("投掷失败")
        
    #     self.navigate_posekey("start") # 返回起始位置
    #     print("返回起始位置")


    # def run(self):
    #     ## 主程序
    #     self.welcome() # 欢迎界面
    #     self.calibratePose("start") # 校准位姿

    #     self.navigate_posekey("CL1")
    #     print("货架")
    #     mail = [1, 0, 100, 0]
    #     response = self.grasp_proxy(*mail)
    #     if response.success:
    #         print("抓取成功")
    #     else:
    #         print("抓取失败")
    #     mail = [0, 1, 100, 0]
    #     response = self.grasp_proxy(*mail)
    #     if response.success:
    #         print("抓取成功")
    #     else:
    #         print("抓取失败")

    #     self.BM.moveForward(1.0, mode="normal") # 前进1.0米
    #     print("前进1.0米")

    #     self.navigate_posekey("LU1")
    #     mail = [1, 0]
    #     response = self.throw_proxy(*mail)
    #     if response.success:
    #         print("投掷成功")
    #     else:
    #         print("投掷失败")

    #     self.navigate_posekey("LU2")
    #     mail = [0, 0]
    #     response = self.throw_proxy(*mail)
    #     if response.success:
    #         print("投掷成功")
    #     else:
    #         print("投掷失败")

    #     self.navigate_posekey("CL5")
    #     print("货架")
    #     mail = [1, 0, 100, 0]
    #     response = self.grasp_proxy(*mail)
    #     if response.success:
    #         print("抓取成功")
    #     else:
    #         print("抓取失败")
    #     mail = [0, 1, 100, 0]
    #     response = self.grasp_proxy(*mail)
    #     if response.success:
    #         print("抓取成功")
    #     else:
    #         print("抓取失败")

       
    #     self.navigate_posekey("LD2")
    #     mail = [1, 0]
    #     response = self.throw_proxy(*mail)
    #     if response.success:
    #         print("投掷成功")
    #     else:
    #         print("投掷失败")

    #     self.navigate_posekey("LD1")
    #     mail = [0, 0]
    #     response = self.throw_proxy(*mail)
    #     if response.success:
    #         print("投掷成功")
    #     else:
    #         print("投掷失败")
        
    #     self.navigate_posekey("start") # 返回起始位置
    #     print("返回起始位置")

    def run(self):
        ## 主程序
        self.welcome() # 欢迎界面
        self.calibratePose("start")
        self.takeshelfPic_L() # 货架拍照左侧
        self.navigate_posekey("start") # 返回起始位置
        
if __name__ == "__main__":
    position_path = "/home/eaibot/nju_ws/src/motion_control/config/position.txt"
    controller = MainController(position_path)
    controller.run()