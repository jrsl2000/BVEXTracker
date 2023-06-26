from time import sleep, time
from numpy import save
from math import floor

try:
	from Sensors.L3GD20H import L3GD20H
except:
	from L3GD20H import L3GD20H

import threading


class Gyro:
	def __init__(self, Write_Directory): #runs upon initialization
		self.wd = Write_Directory
		self.thread = threading.Thread(target=self.run, args=())
		self.alive = True
		self.ih = L3GD20H()
		self.t0 = -1
		self.data = []

		print("gyro initialized")


	def kill(self):
		self.alive=False
		self.thread.join()
		print("gyro ended")

	def begin(self):
		self.thread = threading.Thread(target=self.run, args=())
		self.thread.start()
		self.alive = True
		print("gyro started")

	def save_data(self):
		self.kill()

		assert self.t0 > 0 # make sure data has been collected
		save(self.wd + str(floor(self.t0)), self.data)

		print("gyro data saved, data started at t=", self.t0)

	def run(self):
		self.data = ["time", "gyrox", "gyroy", "gyroz"]
		self.t0 = time()

		while self.alive:
			self.data += self.ih.read_axes()
			sleep(0.001)
	
	def test(self):
		while True:
			t, x, y ,z = self.ih.read_axes()
			print("%8.2f, %8.2f, %8.2f" %(x, y, z))
			sleep(0.001)

if __name__ == "__main__":
	test = Gyro("asd")
	test.test()







