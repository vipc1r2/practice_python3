#coding:utf-8
#程序功能：可以实现抖音个人页面视频的自动点击，从而自动增加访问量
#思路：抖音主页中两个视频切换点击，可以实现访问量的增加
#使用ADB程序，视频的屏幕坐标可以使用adb shell uiautomator dump命令，获取该页面xml源码后查得
#下述是小米MIX2抖音主页第一个视频和第二个视频的坐标位置
#缺点：运行时不能移动屏幕，后续可以采用获取模块ID号的方式去点击相应的位置

import time
import subprocess

'''
import time
import subprocess
i = 0
#每次操作的间隔时间取决于手机配置，配置越高时间越短
sleep_time = 0.5
while 1:
  #用popen设置shell=True不会弹出cmd框
  process = subprocess.Popen('adb shell input tap 14 1402',shell=True)
  time.sleep(sleep_time)
  process = subprocess.Popen('adb shell input keyevent KEYCODE_BACK', shell=True)
  time.sleep(sleep_time)
  process = subprocess.Popen('adb shell input tap 375 1402', shell=True)
  time.sleep(sleep_time)
  process = subprocess.Popen('adb shell input keyevent KEYCODE_BACK', shell=True)
  time.sleep(sleep_time)
  #os.system('adb shell input tap 14 1402')
  #os.system('adb shell input keyevent KEYCODE_BACK')
  #os.system('adb shell input tap 375 1402')
  i+=1
  print str(i) + 'clicks have been completed'

'''

i= 0
sleep_time = 3

while 1:
    # process = subprocess.Popen('adb shell input tap 14 1402', shell=True)
    process = subprocess.Popen('adb shell input tap 900 1250', shell=True)
    time.sleep(sleep_time)

    process = subprocess.Popen('adb shell input keyevent KEYCODE_BACK', shell=True)
    time.sleep(sleep_time)

    i += 1
    print (str(i) + 'clicks have been completed')


