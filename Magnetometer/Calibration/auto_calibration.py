import time
import board
import busio
import numpy as np
from adafruit_lis3mdl import LIS3MDL, Rate
import matplotlib.pyplot as plt

i2c = busio.I2C(board.SCL, board.SDA)
sensor = LIS3MDL(i2c)

current_rate = Rate.RATE_155_HZ
sensor.data_rate = current_rate
start_time = time.monotonic()

time_stamp = time.ctime()

mag1 = []
mag2 = []
mag3 = []
mag_t = []
run_time = 30 # Set run time in seconds

# Magnetometer Calibration #
mag_x, mag_y, mag_z = sensor.magnetic
min_x = max_x = mag_x
min_y = max_y = mag_y
min_z = max_z = mag_z

while True:
	mag_x, mag_y, mag_z = sensor.magnetic
	
	min_x = min(min_x, mag_x)
	min_y = min(min_y, mag_y)
	min_z = min(min_z, mag_z)
		
	max_x = max(max_x, mag_x)
	max_y = max(max_y, mag_y)
	max_z = max(max_z, mag_z)
		
	# Hard Iron Correction
	offset_x = (max_x + min_x)/2.0
	offset_y = (max_y + min_y)/2.0
	offset_z = (max_z + min_z)/2.0
		
	# Soft Iron Correction
	field_x = (max_x - min_x)/2.0
	field_y = (max_y - min_y)/2.0
	field_z = (max_z - min_z)/2.0
	
	
	scale = (field_x + field_y + field_z)/3.0
	
	if field_x != 0 and field_y != 0 and field_z != 0:
		cor_x = scale/field_x
		cor_y = scale/field_y
		cor_z = scale/field_z
		
		mag1.append((mag_x - offset_x)*cor_x)
		mag2.append((mag_y - offset_y)*cor_y)
		mag3.append((mag_z - offset_z)*cor_z)
		mag = np.array([mag1,mag2,mag3],dtype=float)
		mag_t=np.ndarray.transpose(mag)
	else:
		mag1.append((mag_x - offset_x))
		mag2.append((mag_y - offset_y))
		mag3.append((mag_z - offset_z))
		mag = np.array([mag1,mag2,mag3],dtype=float)
		mag_t=np.ndarray.transpose(mag)
	
	#print("Magnetometer: X: {0:8.2f}, Y:{1:8.2f}, Z:{2:8.2f} uT".format(mag_x, mag_y, mag_z))
	print("Hard Offset:  X: {0:8.2f}, Y:{1:8.2f}, Z:{2:8.2f} uT".format(offset_x, offset_y, offset_z))
	print("Field:    X: {0:8.2f}, Y:{1:8.2f}, Z:{2:8.2f} uT".format(field_x, field_y, field_z))
	#print("Corrected:	X:{0:10.2f}, Y:{1:10.2f}, Z:{2:10.2f} uT" .format(mag_x - offset_x, mag_y - offset_y, mag_z - offset_z))
	print("")
	#time.sleep(0.01)
	
	# set sleep time to read value twice per measurement
	sleep_time = 1 / (Rate.string[current_rate] * 2)
	time.sleep(sleep_time)
	
	if (time.monotonic() - start_time) > run_time:
		break

#file_name = 'lis3mdl_mag_data ' + time_stamp # create new file name for every run
#headers = ["X", "Y", "Z (uT)"]
#np.savez(file_name, time_stamp, headers, mag_t) # save to .npz file
#np.savetxt(file_name, mag_t, fmt='%.2f', delimiter='\t', header="{t1}\nX\t\tY\t\tZ (uT)".format(t1=time_stamp), comments='') # save to text file
