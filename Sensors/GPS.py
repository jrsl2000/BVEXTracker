#!/usr/bin/python3
from time import sleep
from numpy import save
from math import floor
from threading import Thread
try:
	from Sensors.gpsModule import ubx, gps_io
except:
	from gpsModule import ubx, gps_io

class Gps:
	def __init__(self, Write_Directory): #runs upon initialization
		self.wd = Write_Directory
		self.thread = Thread(target=self.run, args=())
		self.alive = True
		self.gpsio = gps_io(input_speed=115200) # configured the gps to 115200 baudrate
		self.ih = ubx.ubx()
		self.data = []

		print("gps initialized")


	def kill(self):
		self.alive=False
		self.thread.join()

	def begin(self):
		self.thread = Thread(target=self.run, args=())
		self.thread.start()

	def run(self):
		while self.alive:
			self.data += [self.read()]
			print(self.data)

	def read(self):
		out = None
		while out == None:
			out = self.gpsio.read(self.ih.decode_msg)
		return out


if __name__ == "__main__":
	test = Gps("asd")
	test.begin()
	sleep(1)
	test.kill()
