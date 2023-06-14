#!/usr/bin/env python3

from time import sleep
import threading
from Sensors.Gyroscope import Gyro
from Sensors.GPS import Gps


gyro = Gyro("asd")
gps = Gps("asd")

gyro.begin()
gps.begin()

sleep(3)

gyro.kill()
gps.kill()

print("\nfinished")
