#coding:utf-8
import time
import subprocess
# 京东叠蛋糕

i = 0
sleep_time = 3

# 京东任务
# while (i < 33):
#
#     process = subprocess.Popen('adb shell input tap 900 1250', shell=True)
#     # process = subprocess.Popen('adb shell input tap 900 1450', shell=True)
#     # process = subprocess.Popen('adb shell input tap 900 1650', shell=True)
#     # time.sleep(7)
#     # process = subprocess.Popen('adb shell input swipe 500 1800 500 900 100', shell=True)
#     time.sleep(16)
#
#     process = subprocess.Popen('adb shell input keyevent KEYCODE_BACK', shell=True)
#     time.sleep(sleep_time)
#
#     i += 1
#     print(str(i) + 'clicks have been completed')

# 时光机
# while (i < 33):
#      # process = subprocess.Popen('adb shell input tap 300 650', shell=True)
#      process = subprocess.Popen('adb shell input tap 900 1050', shell=True)
#      time.sleep(3)
#      # process = subprocess.Popen('adb shell input swipe 500 1800 500 900 100', shell=True)
#      time.sleep(3)
#
#      process = subprocess.Popen('adb shell input keyevent KEYCODE_BACK', shell=True)
#      time.sleep(sleep_time)
#
#      i += 1
#      print(str(i) + ' clicks have been completed')

# 拼多多
# for x in range(9):
#     # process = subprocess.Popen('adb shell input tap 950 1400', shell=True)
#     time.sleep(5)
#     for y in range(200):
#         hd1 = subprocess.Popen('adb shell input swipe 500 1800 500 1200 150', shell=True)
#         time.sleep(5)
#         hd1 = subprocess.Popen('adb shell input swipe 500 500 500 1200 150', shell=True)
#         y += 1
#     time.sleep(10)
#     process = subprocess.Popen('adb shell input keyevent KEYCODE_BACK', shell=True)
#     time.sleep(sleep_time)
#     x += 1
#     print('点了按钮第' + str(x) + '次')
#

# 淘宝
#
# while (i < 23):
#
#     process = subprocess.Popen('adb shell input tap 900 1350', shell=True)
#
#     time.sleep(7)
#     # process = subprocess.Popen('adb shell input swipe 500 1800 500 900 100', shell=True)
#     time.sleep(16)
#
#     process = subprocess.Popen('adb shell input keyevent KEYCODE_BACK', shell=True)
#     time.sleep(5)
#
#     i += 1
#     print(str(i) + 'clicks have been completed')
 # 点击小猫
# for x in range(99):
#     process = subprocess.Popen('adb shell input tap 500 1200', shell=True)
#     time.sleep(1)
#     print('点了按钮第' + str(x) + '次')

# while (i < 20):
#      process = subprocess.Popen('adb shell input tap 900 1550', shell=True)
#      time.sleep(7)
#      # process = subprocess.Popen('adb shell input swipe 500 1800 500 900 100', shell=True)
#      time.sleep(16)
#
#      process = subprocess.Popen('adb shell input keyevent KEYCODE_BACK', shell=True)
#      time.sleep(sleep_time)
#
#      i += 1
#      print(str(i) + ' clicks have been completed')
#

 # 考拉
while (i < 20):
      process = subprocess.Popen('adb shell input tap 900 1600', shell=True)
      time.sleep(7)
      process = subprocess.Popen('adb shell input swipe 500 1800 500 900 100', shell=True)
      time.sleep(16)

      process = subprocess.Popen('adb shell input keyevent KEYCODE_BACK', shell=True)
      time.sleep(sleep_time)

      i += 1
      print(str(i) + ' clicks have been completed')

# ---------------------------=============================
# while (i < 20):
#       process = subprocess.Popen('adb shell input tap 900 1600', shell=True)
#       time.sleep(3)
#       process = subprocess.Popen('adb shell input swipe 500 1800 500 900 100', shell=True)
#       time.sleep(6)
#
#       process = subprocess.Popen('adb shell input keyevent KEYCODE_BACK', shell=True)
#       time.sleep(sleep_time)
#
#       i += 1
#       print(str(i) + ' clicks have been completed')