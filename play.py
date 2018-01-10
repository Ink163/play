###!/usr/bin/python
# _*_ coding: utf-8 -*-

from ctypes import *
import time



#def leftlegmove():
 #   maskindex = hex(1<<12)
  #  api.
    
    
#def rightlegmove():
 #   maskindex = hex (1<<7)
  #  api.
    #return hex(1<<7)


#robotname = "Yanshee_8F83"
#timeout = 10 
#loadlib = cdll.LoadLibrary
#api = loadlib("/home/pi/sdk/yanshee-raspi-sdk-master/sdk/librobot.so")
#api.ubtRobotInitialize()




#robotinfo = pointer(UBTEDU_ROBOTINFO_t())
#robotangle = pointer(setangle())

# Search robot for 10 times
#while(timeout > 0):
    #val = api.ubtRobotDiscovery(1,"sdk",robotinfo)
#time = time.time()
   # timeout = timeout - 1
  #  if( robotinfo[0].robotname == robotname ):
 #       break
    
#if val != 0:
   # print("No Robot was found")
 #   time.sleep(5)
  #  exit()

#val = api.ubtRobotConnect("sdk","1",robotinfo[0].robotIP)

#if val != 0:
  #  print("Can not connect !")
 #   exit()






#The robot will move 12 steps
#for i in range(12):
#    if(i % 2 == 0): 
 #       leftlegmove()
  #  else:
   #     rightlegmove()
    #api.ubtrobotservos(indexmask,)
    #i = i + 1


    
#api.ubtDeinitialize()
    
#Test connection

ll = cdll.LoadLibrary
api = ll("/mnt/1xrobot/lib/librobot.so")
api.ubtRobotInitialize()
ret = api.ubtRobotConnect("18682031931","v1.0.9.83-94bbb9326","127.0.0.1")


#Connect the robot
if ret!=0:
    print("Can not connect! Error code: %d" % ret)
    exit(1)
else:
    print("Success!")


#Test the servos
#iIndexMask = 0xfffff
#pcAngle=pointer(SERVOANGLE())
#iAngleLen=sizeof(pcAngle)
#ret = api.ubtGetRobotServo(iIndexMask, pcAngle, iAngleLen)
#print ("Sernos' angle: %s" % (pcAngle))


iIndexMask = 0x02

#for i in range(10):
    

#pcAngle = str("1E")
#ret = api.ubtSetRobotServo(iIndexMask,pcAngle,20)
#if (0 != ret):
 #       print("Failed to call the SDK api. ret %d " % (ret))



#pcAngle = str("1E")
#ret = api.ubtSetRobotServo(iIndexMask,pcAngle,20)
#if (0 != ret):
#    print("Failed to call the SDK api. ret %d " % (ret))




class SERVOSANGLE(Structure):
	_fields_ = [
		("value", c_char*35)
	]
pcAngle=pointer(SERVOSANGLE())
iAngleLen=sizeof(pcAngle)
ret = api.ubtGetRobotServo(iIndexMask, pcAngle, iAngleLen)
if (0 != ret):
	print("Failed to call the SDK api. ret %d " % (ret))



mask = 0x09
for x in range(5):
    mask = 0x09
    
    pcAngle = str("5A")
    ret = api.ubtSetRobotServo(mask,pcAngle,50)
    time.sleep(4)#10ms
    mask =

    #4
    mask = 0x04
    pcAngle = str("55")
    ret = api.ubtSetRobotServo(mask,pcAngle,50)

    #6
    mask = 0x40
    pcAngle = str(hex(int(-90)))
    ret = api.ubtSetRobotServo(mask,pcAngle,50)
    
    pcAngle = str(hex(int(-90)))
    ret = api.ubtSetRobotServo(mask,pcangle,50)
    
    
ret = api.ubtRobotDisconnect("18682031931","v1.0.9.83-94bbb9326","127.0.0.1")
if ret == 0:
    print("Disconnect success !")
api.ubtRobotDeinitialize()    
    
