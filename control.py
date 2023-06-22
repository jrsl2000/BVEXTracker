#!/usr/bin/env python3

from time import sleep
from Sensors.Gyroscope import Gyro
from Sensors.GPS import Gps
from Sensors.IMU import IMU
from Sensors.Accelerometer import Accelerometer


gyro = Gyro("/home/fissellab/BVEXTracker-main/output/Gyroscope/")
gps = Gps("/home/fissellab/BVEXTracker-main/output/GPS/")
imu = IMU("/home/fissellab/BVEXTracker-main/output/IMU/")
acc = Accelerometer("/home/fissellab/BVEXTracker-main/output/Accelerometer/")

try:
	gyro.begin()
	#gps.begin() 
	#imu.begin()

	sleep(3)

	gyro.kill()
	#gps.kill()
	#imu.kill()

except (KeyboardInterrupt):
	gyro.kill()
	gps.kill()
	imu.kill()
	print("\ninterrupt")

	
print("\nfinished")
