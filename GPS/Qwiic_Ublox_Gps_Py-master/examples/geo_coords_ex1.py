#!/usr/bin/env python3
#-----------------------------------------------------------------------------
# geo_coords_ex1.py
#
# Simple Example for SparkFun ublox GPS products 
#------------------------------------------------------------------------
#
# Written by  SparkFun Electronics, July 2020
# 
# Do you like this library? Help support SparkFun. Buy a board!
# https://sparkfun.com
#==================================================================================
# GNU GPL License 3.0
# Copyright (c) 2020 SparkFun Electronics
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#==================================================================================
# Example 1
# This example sets up the serial port and then passes it to the UbloxGPs
# library. From here we call geo_coords() and to get longitude and latitude. I've
# also included heading of motion here as well. 

import serial
import time
import csv
import sys
#sys.path.append('/home/fissellab/BVEX/GPS/Qwiic_Ublox_Gps_Py-master/ublox_gps')
from ublox_gps import UbloxGps

port = serial.Serial('/dev/serial0', baudrate=4800, timeout=1)  # wait for all requested bytes

gps = UbloxGps(port)

timer = 10
end = time.time() + timer

#f = open('/home/fissellab/BVEX/GPS/test_data.csv', 'w')
#writer = csv.writer(f, delimiter=',')

while (time.time() < end):
    data = []

    geo = gps.geo_coords()

    lon = geo.lon
    lat = geo.lat
    alt = geo.height * (10**-3)    # height above ellipsoid m
    velN = geo.velN * (10**-3)   # convert  to m/s
    velE = geo.velE * (10**-3)
    velD = geo.velD * (10**-3)
    timestamp = time.time()
            
    data.append(lon)
    data.append(lat)
    data.append(alt)
    data.append(velN)
    data.append(velE)
    data.append(velD)
    data.append(timestamp)

    
 #   writer.writerow(data)
    
    print(data)
