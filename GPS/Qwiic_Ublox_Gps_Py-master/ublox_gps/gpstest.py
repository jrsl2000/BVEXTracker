import numpy as np
from serial import Serial
import ubx
import csv
import time
import sys
sys.path.insert(1, '/home/fissellab/BVEX/GPS/Qwiic_Ublox_GPS_Py-master/ublox_gps')
from ublox_gps import UbloxGps

port = Serial('/dev/serial0',baudrate=38400, timeout=1)
x = ubx.UbxStream(port)  # change rate with this library

# configure the rate
x.cfg_rate(100)       # delay between reads in ms

x.enable_message(1,7)   # NAV_PVT

#f = open('/home/fissellab/BVEX/GPS/Qwiic_Ublox_Gps_Py-master/ublox_gps/testdata.csv', 'w')
#writer = csv.writer(f, delimiter=',')
    
timer = 5
end = time.time() + timer
    
while (time.time() < end):
	
	pvt = x.read(reset=False)  # pollsh
	
	data = []
	
	lon = pvt.lon
	lat = pvt.lat
	alt = pvt.height
	timestamp = pvt.iTOW
	data.append(lon)
	data.append(lat)
	data.append(alt)
	#data.append(velN)
	#data.append(velE)
	#data.append(velD)
	data.append(timestamp)
        
	#writer.writerow(data)
    
	print(data)
	time.sleep(0.01)


