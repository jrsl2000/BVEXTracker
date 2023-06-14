from time import sleep
from L3GD20H import L3GD20H
import threading


class Gyro:
	def __init__(self, Write_Directory): #runs upon initialization
		self.wd = Write_Directory
		self.thread = threading.Thread(target=self.run, args=())
		self.alive = True
		self.interface_handler = L3GD20H()

		print("gyro initialized")
		
		
	def kill(self):
		self.alive=False
		self.thread.join()
		
	def begin(self):
		self.thread.start()
		
	def run(self):
		while self.alive:
			gyrodata = self.interface_handler.read_axes()
			print(gyrodata)
			sleep(1)
		
if __name__ == "__main__":
	test = Gyro("asd")
	test.begin()
	sleep(2)
	test.kill()
	
