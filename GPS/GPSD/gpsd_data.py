                                                                                                                                   #! /usr/bin/python
from gps import *
import time
import csv
import numpy as np
from datetime import datetime

"""
Can sample at 20 Hz, change sampling of gpsd by typing "gpsctl -c 0.05" in terminal

"""

gpsd = gps(mode=WATCH_ENABLE|WATCH_NEWSTYLE)

timer = 2        # change this for different times
end = time.time() + timer

datalist = []
try:
    while (time.time() < end):
        report = gpsd.next() 
        print(report)
        
        data = []
        
        if False:#report['class'] == 'TPV':
            if str(getattr(report, 'mode', 3)):  # check there's a fix
                  lon = str(getattr(report,'lat', 'nan'))         #degrees
                  lat = str(getattr(report,'lon','nan'))          # degrees
                  alt = str(getattr(report,'altHAE','nan'))       #height above ellipsoid (meters)
                  ecefvx = str(getattr(report, 'ecefvx', 'nan'))  # earth centered, earth-fixed -> origin is ellipsoid
                  ecefvy = str(getattr(report, 'ecefvy', 'nan'))
                  ecefvz = str(getattr(report, 'ecefvz', 'nan'))
                  gps_time = str(getattr(report, 'time', 'nan'))
                  timestamp = time.time()
        
                  data.append(timestamp)
                  data.append(gps_time)
                  data.append(lon)
                  data.append(lat)
                  data.append(alt)
                  data.append(ecefvx)
                  data.append(ecefvy)
                  data.append(ecefvz)
            
                  datalist.append(data)
            
                  time.sleep(0.05)  # 50ms delay 
            
            
except (KeyboardInterrupt, SystemExit): #when you press ctrl+c
    print ("Done.\nExiting.")
  
dataarr = np.array(datalist)

time = dataarr[:,0]
gps_time = dataarr[:,1]
longitude = dataarr[:,2]
latitude = dataarr[:,3]
HAE = dataarr[:,4]  # height above ellipsoid
vx = dataarr[:,5]
vy = dataarr[:,6]
vz = dataarr[:,7]    # velocities are in ECEF coord system

# change for different filename
#f = open('/home/fissellab/BVEX/GPS/GPSD/test.csv', 'w')
#writer = csv.writer(f, delimiter=',')

# save to .npz file
np.savez('/home/fissellab/BVEX/GPS/GPSD/gpsdata', time, gps_time, longitude, latitude, HAE, vx, vy, vz)
