from time import sleep, time
from adafruit_extended_bus import ExtendedI2C as I2C
import threading
import numpy as np
from math import floor

try:
	import Sensors.adafruit_bno055 as bno055
except:
	import adafruit_bno055 as bno055

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

class IMU:
	def __init__(self, Write_Directory):
		self.wd = Write_Directory
		self.thread = None 
		self.alive = True
		self.ih = bno055.BNO055_I2C(I2C(1)) # ih = interface handler
		self.data=[]
		self.t0 = -1
		print("IMU initialized")
	
	def kill(self):
		self.alive = False
		self.thread.join()
		print("IMU ended")
		
	def begin(self):
		self.thread = threading.Thread(target=self.run, args=())
		self.thread.start()
		print("IMU started")
	
	def save(self):
		self.kill()
		self.thread.join()
		
		assert self.t0 > 0 # make sure data has been collected
		           # filename 				item to save
		np.save(self.wd + str(floor(self.t0)), flatten_list(self.data))

		print("IMU data saved, data started at t=", self.t0)
	
	def run(self):
		self.data = [] # clears data 
		self.t0 = time()
		while self.alive:
			self.data += [time(),
			self.ih.acceleration,
			self.ih.magnetic,
			self.ih.gyro,
			self.ih.euler,
			self.ih.quaternion,
			self.ih.linear_acceleration,
			self.ih.gravity]
		
		#self.save()

if __name__ == "__main__":
	test = IMU("/home/fissellab/BVEXTracker-main/output/IMU/")
	test.begin()
	sleep(2)
	test.save()
	sleep(2)
	#test.save()
	test.kill()
	
	
