import time
import os
import numpy as np
from adafruit_lis3mdl import LIS3MDL, Rate
from adafruit_extended_bus import ExtendedI2C as I2C
import matplotlib.pyplot as plt

i2c = I2C(1)  # Device is /dev/i2c-1
sensor = LIS3MDL(i2c)

#i2c = busio.I2C(board.SCL, board.SDA)
#sensor = LIS3MDL(i2c)

current_rate = Rate.RATE_155_HZ
sensor.data_rate = current_rate

mag1 = []
mag2 = []
mag3 = []
mag_t = []
t = []

file_name = 'Magnetometer'
headers = ["UTC Time (s)", "X (uT)", "Y (uT)", "Z (uT)"]

start_time = time.monotonic()
start_save_time = time.monotonic()
run_time = 10 # seconds
save_time = 10.0 # Time increment, in seconds, for saving data files

while True:
	print(sensor.magnetic)
	mag_x, mag_y, mag_z = sensor.magnetic
	
	# UTC timestamp as float
	timestamp = time.time()
	t.append(timestamp)
	
	# Magnetic field components
	mag1.append(mag_x)
	mag2.append(mag_y)
	mag3.append(mag_z)
	
	# Combine time and magnetic field
	mag = np.array([t,mag1,mag2,mag3],dtype=float)
	mag_t=np.ndarray.transpose(mag)
	
	# Set sleep time to read value twice per measurement
	sleep_time = 1 / (Rate.string[current_rate] * 2)
	time.sleep(sleep_time)
	
	'''# Create a new directory and save data to binary files every 10 minutes
	if (time.monotonic() - start_save_time) >= save_time:
		
		# Create directory 'day_month_year_hr-min-sec' in parent_dir
		time_stamp = time.strftime("%d%b%Y_%H_%M_%S", time.gmtime())
		directory = "{}".format(time_stamp)
		parent_dir = ""
		path = os.path.join(parent_dir, directory)
		#os.mkdir(path)
		print("Directory '% s' created" % directory)
		
		# Save data files to new directory
		#home_dir = os.getcwd()
		#os.chdir(path)
		#np.savez(file_name, headers, mag_t) # save to .npz file
		#os.chdir(home_dir)

		# Reset data arrays
		mag1 = []
		mag2 = []
		mag3 = []
		mag_t = []
		t = []
		
		start_save_time = time.monotonic() # Reset time'''
	
	# Save data and terminate data logging after run_time
	if (time.monotonic() - start_time) > run_time:
		
		# Create directory 'day_month_year_hr-min-sec' in parent_dir
		#time_stamp = time.strftime("%d%b%Y_%H_%M_%S", time.gmtime()) # Format timestamp in UTC
		#directory = "{}".format(time_stamp)
		#parent_dir = ""
		#path = os.path.join(parent_dir, directory)
		#os.mkdir(path)
		#print("Directory '% s' created" % directory)
		
		# Save data files to new directory
		#home_dir = os.getcwd()
		#os.chdir(path)
		#np.savez(file_name, headers, mag_t) # save to .npz file
		#os.chdir(home_dir)
		
		break # Terminate data logging

#time_stamp = time.strftime("%d%b%Y_%H_%M_%S", time.gmtime()) # Format timestamp in UTC
#file_name = 'Magnetometer ' + time_stamp # create new file name for every run
#headers = ["Timestamp(s)", "X(uT)", "Y(uT)", "Z(uT)"]
#np.savez(file_name, headers, mag_t) # save to .npz file
#	np.savetxt(file_name, mag_t, delimiter=',', header="{t1}\nTimestamp(s)\tX(uT)\tY(uT)\tZ(uT)".format(t1=time_stamp), comments='') # save to text file
