import spidev
import time
import numpy as np
import sys

import adxl355
from datetime import datetime
import csv
import time

# Initialize the SPI interface                                                 
spi = spidev.SpiDev()
bus = 0
cs = 0  # change this for different chip select pins
spi.open(bus, cs)
spi.max_speed_hz = 10000000
spi.mode = 0b00 #ADXL 355 has mode SPOL=0 SPHA=0, its bit code is 0b00

# possible data rate: 4000, 2000, 1000, 500, 250, 125, 62.5, 31.25, 15.625, 7.813, 3.906 
rate = 1000

# Initialize the ADXL355                                                       
acc = adxl355.ADXL355(spi.xfer2)
acc.start()
acc.setrange(adxl355.SET_RANGE_2G) # set range to 2g
acc.setfilter(lpf = adxl355.ODR_TO_BIT[rate]) # set data rate

# data read from fifo saves as one list, this function saves every n items to one row in csv
def chunks(lst, n):
	for i in range(0, len(lst), n):
		yield lst[i: i+n]
		
# Record data 
ntime = 10               # comment sampling time in seconds
end = time.time() + ntime
samples = ntime * rate * 4   # 4 columns of data

acc.emptyfifo()  # make sure fifo is empty first before reading

datalist = []
while (time.time() < end):   # is exactly 1000 Hz

	if acc.hasnewdata():
		datalist += acc.fastgetsamples(samples) # returns readings from the fifo and append to list

# datalist returns one single list but want 4 columns of data
newlist = []
for y in chunks(datalist, 4):
	newlist.append(y)

# convert to array
dataarr = np.array(newlist)

# subtract the offset values
xoffset = -0.007815115289
yoffset = -0.005857900037
zoffset = -0.012328876967

xdata = dataarr[:,1] - xoffset
ydata = dataarr[:,2] - yoffset
zdata = dataarr[:,3] - zoffset

# save to csv
#f = open('/home/fissellab/BVEX/accelerometer/accel_data/-z/-z_1.csv', 'w')
#writer = csv.writer(f, delimiter=',')
#writer.writerow(dataarr[0])            # write down first line of data with timestamp
#writer.writerows(dataarr[1:-1, 0:3])   # don't write timestamp column
#writer.writerow(dataarr[-1])           # write last line of data with timestamp

# save to npz file
# np.savez saves each dataset as an array
np.savez('/home/fissellab/BVEX/accelerometer/output', dataarr[::len(dataarr)-1, 0], xdata, ydata, zdata)  # first and last timestamp of first column


