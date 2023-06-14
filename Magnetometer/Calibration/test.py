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

run_time = 10 # Set run time in seconds
offset = []
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

	field_x = (max_x - min_x)/2.0
	field_y = (max_y - min_y)/2.0
	field_z = (max_z - min_z)/2.0
		
	print("Magnetometer: X: {0:8.2f}, Y:{1:8.2f}, Z:{2:8.2f} uT".format(mag_x, mag_y, mag_z))
	print("Hard Offset:  X: {0:8.2f}, Y:{1:8.2f}, Z:{2:8.2f} uT".format(offset_x, offset_y, offset_z))
	print("Field:    X: {0:8.2f}, Y:{1:8.2f}, Z:{2:8.2f} uT".format(field_x, field_y, field_z))
	print("")
	time.sleep(0.01)
	
	# set sleep time to read value twice per measurement
	sleep_time = 1 / (Rate.string[current_rate] * 2)
	time.sleep(sleep_time)
	
	if (time.monotonic() - start_time) > run_time:
		offset.append(offset_x)
		offset.append(offset_y)
		offset.append(offset_z)
		break

mag1 = []
mag2 = []
mag3 = []
magt = []
t = []
start_time = time.monotonic()


while True:
	mag_x, mag_y, mag_z = sensor.magnetic
	
	# Get timestamp
	timestamp = time.time()
	t.append(timestamp)
	
	# Get magnetic field components
	mag1.append(mag_x - offset[0])
	mag2.append(mag_y - offset[1])
	mag3.append(mag_z - offset[2])
	
	# Combine time and magnetic field
	mag = np.array([t,mag1,mag2,mag3],dtype=float)
	mag_t=np.ndarray.transpose(mag)
	
	# Set sleep time to read value twice per measurement
	sleep_time = 1 / (Rate.string[current_rate] * 2)
	time.sleep(sleep_time)
	
	# Save data to a binary file every 10 minutes
	#if (time.monotonic() - start_save_time) > save_time:
		#time_stamp = time.ctime()
		#print("Saved to file", time_stamp)
		#file_name = 'lis3mdl_mag_data ' + time_stamp
		#headers = ["UTC Time (s)", "X (uT)", "Y (uT)", "Z (uT)"]
		#np.savez(file_name, headers, mag_t) # save to .npz file
		#start_save_time = time.monotonic() # Reset time		
	
	# Terminate data logging after run_time
	if (time.monotonic() - start_time) > run_time:
		break

fig, ax = plt.subplots(1,1)
ax.set_aspect(1)
ax.scatter(mag1, mag2, color = 'darkorange', label = 'XY')
ax.scatter(mag2, mag3, color = 'seagreen', label = 'YZ')
ax.scatter(mag3, mag1, color = 'royalblue', label = 'ZX')
ax.legend()
	
time_x = np.linspace(0, run_time, len(mag1)) # create time array for x axis
fig1, ax1 = plt.subplots(1)
ax1.plot(time_x, mag1, color = 'darkorange', label = 'X')
ax1.plot(time_x, mag2, color = 'seagreen', label = 'Y')
ax1.plot(time_x, mag3, color = 'royalblue', label = 'Z')
ax1.legend()
	
plt.show()	

