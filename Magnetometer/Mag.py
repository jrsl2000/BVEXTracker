import time
import os
import numpy as np
from adafruit_lis3mdl import LIS3MDL, Rate
from adafruit_extended_bus import ExtendedI2C as I2C
import matplotlib.pyplot as plt

def init_mag():
	
	i2c = I2C(1)  # Device is /dev/i2c-1
	sensor = LIS3MDL(i2c)

	current_rate = Rate.RATE_155_HZ
	sensor.data_rate = current_rate
	if True:
		init = 1
	return init

def run_mag():
	mag1 = []
	mag2 = []
	mag3 = []
	mag_t = []
	
	start_time = time.monotonic()
	run_time = 10 #seconds
	
	while True:
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
	
		if (time.monotonic() - start_time) > run_time:
			break
	return mag_t

def get_mag_header():
	headers = ["time(s)", "mx(uT)", "my(uT)", "mz(uT)"]
	return headers


def get_mag_temp():
	temp = 1
	return temp

print(run_mag())
