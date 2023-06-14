# Angles of magnetic field in degrees
import time
from math import atan2, degrees
import board
from adafruit_lis3mdl import LIS3MDL, Rate
import numpy as np

i2c = board.I2C()
sensor = LIS3MDL(i2c)

current_rate = Rate.RATE_155_HZ
sensor.data_rate = current_rate
start_time = time.monotonic()
time_stamp = time.ctime()

def vector_2_degrees(x,y,z):
	angle1 = degrees(atan2(y,x)) # Declination
	angle2 = degrees(atan2(z,x)) # Inclination
	angle3 = degrees(atan2(z,y))
	if angle1 < 0:
		angle1 += 360
	if angle2 < 0:
		angle2 += 360
	if angle3 < 0:
		angle3 += 360
	return angle1, angle2, angle3

def get_heading(_sensor):
	magnet_x, magnet_y, magnet_z = _sensor.magnetic
	return vector_2_degrees(magnet_x, magnet_y, magnet_z)

angle = []
run_time = 10

while True:
	theta1, theta2, theta3 = get_heading(sensor)
	angle.append(theta1)
	angle.append(theta2)
	angle.append(theta3)
	print("Angles XY: {:.2f} XZ: {:.2f} YZ: {:.2f} degrees".format(theta1,theta2,theta3))
	
	sleep_time = 1 / (Rate.string[current_rate] * 2)
	time.sleep(sleep_time)
	
	if (time.monotonic() - start_time) > run_time:
		break
#file_name = 'lis3mdl_heading' + time_stamp # create new file name for every run
#headers = ["Heading (deg)"]
#np.savez(file_name, time_stamp, headers, angle) # save to .npz file
#np.savetxt(file_name, angle, fmt='%.2f', delimiter='\t', header="{t1}\nHeading (deg)".format(t1=time_stamp), comments='') # save to text file
