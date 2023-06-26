import os
import numpy as np
from adafruit_lis3mdl import LIS3MDL, Rate
from adafruit_extended_bus import ExtendedI2C as I2C
import matplotlib.pyplot as plt
from time import sleep, time
from adafruit_extended_bus import ExtendedI2C as I2C
import threading
from math import floor
from numpy import save
try:
    import Sensors.adafruit_bno055 as bno055
except:
    import adafruit_bno055 as bno055

i2c = I2C(1)  # Device is /dev/i2c-1
mag = LIS3MDL(i2c)
imu = bno055.BNO055_I2C(i2c)
current_rate = Rate.RATE_155_HZ
mag.data_rate = current_rate
t = []

mag1 = []
mag2 = []
mag3 = []
imu1 = []
imu2 = []
imu3 = []
t = []

t0 = time()
while time() < t0 + 15:
    # both measure magentic field
    
    mag_x, mag_y, mag_z = mag.magnetic
    imu_x, imu_y, imu_z = imu.magnetic
    
    mag1.append(mag_x)
    mag2.append(mag_y)
    mag3.append(mag_z)
    imu1.append(imu_x)
    imu2.append(imu_y)
    imu3.append(imu_z)
    t.append(time())
    print("mag; imu\n%5.2f, %5.2f, %5.2f\n%5.2f, %5.2f, %5.2f" %(mag_x,mag_y,mag_z,imu_x,imu_y,imu_z))

    # Set sleep time to read value twice per measurement
    sleep_time = 1 / (Rate.string[current_rate] * 2)
    sleep(sleep_time)

fig, ax = plt.subplots(3)

ax[0].plot(t, mag1, label="mag1")
ax[0].plot(t, imu1, label="imu1")
ax[0].legend()

ax[1].plot(t, mag2, label="mag2")
ax[1].plot(t, imu2, label="imu2")
ax[1].legend()

ax[2].plot(t, mag3, label="mag3")
ax[2].plot(t, imu3, label="imu3")
ax[2].legend()

plt.show()
