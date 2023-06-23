#!/usr/bin/python3
from gps import ubx
from time import sleep
from numpy import save
from math import floor
import threading


class Gps:
	def __init__(self, Write_Directory): #runs upon initialization
		self.wd = Write_Directory
		self.thread = threading.Thread(target=self.run, args=())
		self.alive = True
		self.interface_handler = gps(mode=WATCH_ENABLE)

		print("gyro initialized")
		
		
	def kill(self):
		self.alive=False
		self.thread.join()
		
	def begin(self):
		self.thread.start()
		
	def run(self):
		while self.alive:
			report = self.interface_handler.next()
			print(report)
			sleep(1)
		
if __name__ == "__main__":
	test = Gps("asd")
	test.begin()
	
	
