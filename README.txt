# camera 摄像头
# dobot 机械臂
# motion_control 运动控制

roslaunch dashgo_nav navigation_imu_2.launch
roslaunch motion_control main_process.launch

# 省份字母编码：江苏 js 浙江 zj 安徽 ah 河南 he 湖南 hu 四川 sc 广东 gd 福建 fj 无效 wx
# 省份数字编码：江苏 1  浙江 2  安徽 3  河南 4  湖南 5  四川 6  广东 7  福建 8  无效 0

#左 1/1.1 1/1.2 2/1.3 2/1.4 3/1.5 中 4/1.6 5/1.7 5/1.8 6/1.9 6/1.10 右
#左 1/2.1 1/2.2 2/2.3 2/2.4 3/2.5 中 4/2.6 5/2.7 5/2.8 6/2.9 6/2.10 右