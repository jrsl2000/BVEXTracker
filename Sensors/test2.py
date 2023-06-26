from time import sleep, time
from adafruit_extended_bus import ExtendedI2C as I2C
import threading
from math import floor
from numpy import save
from struct import pack

try:
	import Sensors.adafruit_bno055 as bno055
except:
	import adafruit_bno055 as bno055

imu = bno055.BNO055_I2C(I2C(1))

file = open("binDat", "wb")

for i in range(10):
	for e in imu.acceleration:
		print(type(e))
		file.write(pack('f', e))

file.close()
