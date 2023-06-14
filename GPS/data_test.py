import numpy as np

f = '/home/fissellab/BVEX/GPS/gpsdata.npz'
npzfile = np.load(f)
print(npzfile['arr_0'])
print(npzfile['arr_1'])
print(npzfile['arr_2'])
print(npzfile['arr_3'])
print(npzfile['arr_4'])
print(npzfile['arr_5'])
print(npzfile['arr_6'])
	 
