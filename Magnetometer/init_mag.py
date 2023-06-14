from time import sleep
import numpy as np
from adafruit_lis3mdl import LIS3MDL, Rate
from adafruit_extended_bus import ExtendedI2C as I2C

'''adafruit_lis3mdl.py'''

# init lis3mdl and start temp sensor
i2c = I2C(1)
sensor = LIS3MDL(i2c)
LIS3MDL.__init__(sensor, i2c)
print(LIS3MDL.__init__(sensor,i2c))
print(sensor.temp_enable)
sleep(0.1)

### get magnetometer data ###
header = ["mx", 'my', 'mz', 'temp']
print(header)
while True:
	print(sensor.magnetic)
	print(sensor.get_temp)
	
	#print(magx, magy, magz, "%.2f" %sensor.get_temp)
	sleep(0.2)
