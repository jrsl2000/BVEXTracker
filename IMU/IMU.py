# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

"""
This example demonstrates how to instantiate the
Adafruit BNO055 Sensor using this library and just
the I2C bus number.
This example will only work on a Raspberry Pi
and does require the i2c-gpio kernel module to be
installed and enabled. Most Raspberry Pis will
already have it installed, however most do not
have it enabled. You will have to manually enable it
"""

import time
import csv
import numpy as np
from adafruit_extended_bus import ExtendedI2C as I2C
import adafruit_bno055
from datetime import datetime

# To enable i2c-gpio, add the line `dtoverlay=i2c-gpio` to /boot/config.txt
# Then reboot the pi

# Create library object using our Extended Bus I2C port
# Use `ls /dev/i2c*` to find out what i2c devices are connected
i2c = I2C(1)  # Device is /dev/i2c-1
sensor = adafruit_bno055.BNO055_I2C(i2c)

last_val = 0xFFFF

f = open('/home/fissellab/BVEX/IMU/test.csv', 'w')
writer = csv.writer(f, delimiter=',')
writer.writerow(['timestamp','ax', 'ay', 'az', 'mx', 'my', 'mz','gx', 'gy', 'gz', 'ex',
				'ey', 'ez', 'qw', 'qx', 'qy', 'qz', 'lx', 'ly', 'lz', 'grx', 'gry', 'grz', 'temperature' ])

# function to get rid of nested lists        
def flatten_list(_list):
	flat_list = []
	for element in _list:
		if type(element) is list:
			for item in element:
				flat_list.append(item)
		else:
			flat_list.append(element)
	return flat_list

# writing multiple items in one row to csv 	
def chunks(lst, n):
	for i in range(0, len(lst), n):
		yield lst[i: i+n]

# return the temperature
def temperature():
	global last_val  # pylint: disable=global-statement
	result = sensor.temperature
	if abs(result - last_val) == 128:
		result = sensor.temperature
		if abs(result - last_val) == 128:
			return 0b00111111 & result
	last_val = result
	
	return result


timer = 10
end = time.time() + timer
t0 = time.time()

datalist = []
while (time.time() < end):
	print(sensor.acceleration)
	data = []
	
	#accel = list(sensor.acceleration)  # returns tuples so convert to list
	#mag = list(sensor.magnetic)
	#gyro = list(sensor.gyro)
	#euler = list(sensor.euler)
	#quat = list(sensor.quaternion)
	#linaccel = list(sensor.linear_acceleration)
	#grav = list(sensor.gravity)
	
	#timestamp = time.time() 
	
	#data.append(timestamp)
	#data.append(accel)
	#data.append(mag)
	#data.append(gyro)
	#data.append(euler)
	#data.append(quat)
	#data.append(linaccel)
	#data.append(grav)

	#data = flatten_list(data)  # get rid of nested lists
	#datalist.append(data)      # append this to list outside of loop
	
	time.sleep(0.005)

# save temp data to separate list that returns temperature every 1 Hz (if at 100, every 10 samples)
tempdata = []
while (len(tempdata) < len(datalist)):
	temp = temperature()
	for i in range(len(datalist)):
		if i % 10 == 0:            # return temperature for every 10 samples
			tempdata.append(temp)
		else:                      # return nan for in between
			tempdata.append(np.nan)

dataarr = np.array(datalist)
temparr = np.array(tempdata)
temparr = np.reshape(temparr, (len(temparr), 1))
alldata = np.append(dataarr, temparr, axis=1)     # append temp data as a column onto the rest of the data

writer.writerows(alldata)

 

# look at the euler angles and gps output for orientation
