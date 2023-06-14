import time
import numpy as np
import csv
import matplotlib.pyplot as plt

from L3GD20H import L3GD20H

gyro = L3GD20H()

timer = 5 # seconds
end = time.time() + timer

datalist = []  # define empty list
while (time.time() < end):
	
	gyrodata = gyro.read_axes()  # read gx, gy and gz from L3GD20H class
	datalist.append(gyrodata)    
	print(gyrodata)
	time.sleep(1)  # gyro needs 1 ms delay between reads or else won't sample properly

# convert to array
dataarr = np.array(datalist)

# save to csv file for now
#f = open('/home/fissellab/BVEX/gyroscope/gyrodata/offsets_9.csv', 'w')
#writer = csv.writer(f, delimiter=',')
#writer.writerows(datalist)
		
# save to .npz file
# saving gx, gy, gz and time as their own data arrays 
np.savez('/home/fissellab/BVEX/gyroscope/gyro_bin', dataarr[:,0], dataarr[:,1], dataarr[:,2], dataarr[:,3])
