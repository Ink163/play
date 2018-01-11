###!/usr/bin/python
# _*_ coding: utf-8 -*-

from ctypes import *
import time



    
#api.ubtDeinitialize()
    
#Test connection

ll = cdll.LoadLibrary
api = ll("/mnt/1xrobot/lib/librobot.so")
api.ubtRobotInitialize()
ret = api.ubtRobotConnect("13825237954","v1.0.9.83-94bbb9326","127.0.0.1")


#Connect the robot
if ret!=0:
    print("Can not connect! Error code: %d" % ret)
    exit(1)
else:
    print("Success!")




class SERVOANGLE(Structure):
    _fields_ = [
        ("value", c_char * 35)
        ]



def movement_1():
    mask_6 = 0x20
    mask_3 = 0x04
    
    set_6_Angle = "1E"
    api.ubtSetRobotServo(mask_6,set_6_Angle,50)


    set_3_Angle = "96"
    api.ubtSetRobotServo(mask_3,set_3_Angle,50)


    set_6_Angle = "5A"
    api.ubtSetRobotServo(mask_6,set_6_Angle,50)


    set_3_Angle = "5A"
    api.ubtSetRobotServo(mask_3,set_3_Angle,50)


def movement_2():
    mask = 0x01
    angle = "00"
    api.ubtSetRobotServo(mask,angle,500)
    mask = 0x08
    angle = "B4"
    api.ubtSetRobotServo(mask,angle,500)
    x = 0
    time.sleep(5)
    
    for x in range(2):
        movement_1()
        time.sleep(1)
        x = x + 1
        
    time.sleep(3)
    
    angle = "5A"
    api.ubtSetRobotServo(mask,angle,500)
    mask = 0x01
    api.ubtSetRobotServo(mask,angle,500)
    



def reset():
    mask = 0x01
    angle = "5A"
    api.ubtSetRobotServo(mask,angle,500)
    mask = 0x08
    api.ubtSetRobotServo(mask,angle,500)

# My Movement
#reset()
movement_2()





#ret = api.ubtRobotDisconnect("13825237954","v1.0.9.83-94bbb9326","127.0.0.1")
#if ret == 0:
 #   print("Disconnect success !")
#api.ubtRobotDeinitialize()    
    
