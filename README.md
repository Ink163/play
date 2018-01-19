# yanshee-raspi-sdk


### Overiew of the Yanshee-raspi-sdk(Yanshee-sdk)

The Yanshee-sdk provides arm-linux based c and python library that allows developers to control yanshee robot


### Hardware
 
1. Yanshee robot(Ex. Raspberry Pi 3 Main board)
2. Monitor
3. Output cable (Ex. HDMI-DVI/HDMI-VGA/HDMI-HDMI)
4. USB cable/wireless(Recommond)  mouse
5. Stick sensors(Ex. infrared sensor) 


### Software

1. Ex. noobs developing system
[Go to official website] (https://www.raspberrypi.org/downloads/noobs/) 


### Get started


1: Prepare your workspace and download the SDK

Commond(download): "git clone https://github.com/UBTEDU/yanshee-raspi-sdk.git" <br>


2: Compile the files

Commond: "make" (PS: MAKE IN THE FOLDER /yanshee-raspi-sdk)



3: Set up dynamic library path 

Commond: "export LD_LIBRARY_PATH=(The path for the librobot.so):$LD_LIBRARY_PATH"



4: Get the example 

Find the demonstration python scripts in folder /sdk/example/python



5: Execute and learn the example 

Commond: "python (example name).py".

PS: Make sure the python scripts and "RobotApi.c";"RobotApi.h";"RobotApi.i";"RobotApi.o";"RobotApi.py";"_RobotApi.so". 
are in same folder! 


6: Build your own project