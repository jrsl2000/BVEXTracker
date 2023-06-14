import board
from adafruit_lis3mdl import LIS3MDL, Rate
import smbus
import time
import numpy as np

i2c = board.I2C()
sensor = LIS3MDL(i2c)

bus = smbus.SMBus(1)

# Set Data Rate
current_rate = Rate.RATE_155_HZ
sensor.data_rate = current_rate
start_time = time.monotonic()

time_stamp = time.ctime()

LIS3MDL_M_ADDRESS = 0x1C
LIS3MDL_CTRL_REG1_M = 0x20
LIS3MDL_REG_CTL_1_TEMP_EN = 0x80
TEMP_OUT_L = 0x2E
TEMP_OUT_H = 0x2F

class LIS3MDL:
	def initialize():
		bus.write_byte_data(LIS3MDL_M_ADDRESS, LIS3MDL_CTRL_REG1_M, LIS3MDL_REG_CTL_1_TEMP_EN)
		time.sleep(0.1)
		
	def read_temp():
		Temp_l = bus.read_byte_data(LIS3MDL_M_ADDRESS,TEMP_OUT_L)
		Temp_h = bus.read_byte_data(LIS3MDL_M_ADDRESS,TEMP_OUT_H)
		Temp_total = (Temp_h << 8) | Temp_l
		if Temp_total > 32767:
			Temp_total -= 65536
		cTemp = (Temp_total * 0.125) + 25.0 # Divide by 8 then add the base temperature (25 Celsius when reading is zero)
		return cTemp

temp = []

while True:
	LIS3MDL.initialize() # Enable temperature sensor
	Temperature = LIS3MDL.read_temp() # Get temperature in Celsius
	temp.append(Temperature)

	degree_sign = u"\N{DEGREE SIGN}"
	print("Temperature: %.2f" %Temperature, "{}C".format(degree_sign))
	
	# set sleep time to read value twice per measurement
	sleep_time = 1 / (Rate.string[current_rate] * 2)
	time.sleep(sleep_time)

	if (time.monotonic() - start_time) > 10: # set run time in seconds
		break

# Save data to .npz and .txt files
#file_name = 'lis3mdl_temp_data ' + time_stamp # create new file name for every run
#headers = ["Temperature {}C".format(degree_sign)]
#np.savez(file_name, time_stamp, headers, temp) # save to .npz file
#np.savetxt(file_name, temp, fmt='%.2f', header="Temperature {}C".format(degree_sign), comments='') # save to text file
