import spidev
import numpy as np
from adxl355 import ADXL355, SET_RANGE_2G, ODR_TO_BIT
from datetime import datetime
import csv
from time import time, sleep
import threading
from math import floor

# function to get rid of nested lists        
def flatten_list(_list):
	flat_list = []
	for element in _list:
		if hasattr(element, '__iter__'): # if the item is iterable
			for item in element:
				flat_list.append(item)
		else:
			flat_list.append(element)
	return flat_list

class Accelerometer:
	def __init__(self, Write_Directory, rate=4000):
		self.wd = Write_Directory
		self.thread = None
		self.alive = True
		self.data= []
		self.t0 = -1
		self.rate = rate # valid: 4000, 2000, 1000, 500, 250, 125
		
		# SETUP SPI AND ACCELEROMTERE
		spi = spidev.SpiDev()
		spi.open(0, 0) # bus=0, cs=0
		spi.max_speed_hz = 10000000
		spi.mode = 0b00
		self.interface_handler = ADXL355(spi.xfer2)
		self.interface_handler.start()
		self.interface_handler.setrange(SET_RANGE_2G) # set range to 2g
		self.interface_handler.setfilter(lpf = ODR_TO_BIT[rate]) # set data rate
		#self.interface_handler.dumpinfo()
		print("accelerometer initialized")
		
	def kill(self):
		self.alive=False
		self.thread.join()
		
	def begin(self):
		self.thread  = threading.Thread(target=self.run, args=())
		self.thread.start()
		
	def save(self):
		self.kill()
		self.thread.join()
		print("beginning save")
		t1 = time()
		assert self.t0 > 0 # make sure data has been collected
		           # filename 				item to save
		np.save(self.wd + str(floor(self.t0)), flatten_list(self.data))
		print("time to save: ", time() - t1)


	def run(self):
		self.data = []		
		self.t0 = time()
		try:
			while self.alive:
				self.data += self.interface_handler.get3Vfifo()
		except (OverflowError):
			print("too much data, overflow error")
			self.kill()
			

if __name__ == "__main__":
	test = Accelerometer("/home/fissellab/BVEXTracker-main/output/Accelerometer/")
	test.begin()
	sleep(60)
	test.save()
	test.kill()
	

