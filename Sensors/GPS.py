#!/usr/bin/python
from gps import *
import time

"""
Can sample at 20 Hz, change sampling of gpsd by typing "gpsctl -c 0.05" in terminal
"""

from time import sleep
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
	sleep(2)
	test.kill()
	
