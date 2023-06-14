import numpy as np 
import glob
from statistics import mean

# load files then calculate the mean for each axis
def calc_mean(filename):
	data = np.loadtxt(filename, delimiter=',', usecols=(0,1,2))
	
	x = data[1:-1,0]  # first and last rows have timestamps
	y = data[1:-1,1]
	z = data[1:-1,2]
		
	xmean = np.mean(x)
	ymean = np.mean(y)
	zmean = np.mean(z)
	
	mean_list = [xmean, ymean, zmean]
	
	return mean_list  # return list so can slice for x y or z
	
def xoffsets(data_files):
	
	xmean = []
	for i in data_files:              # for every file in the folder
		xyz_offsets = calc_mean(i)
		xmean.append(xyz_offsets[0])  # append x mean values
		
	total_xoffset = np.mean(xmean)    # take the mean from all 10 runs
	
	return total_xoffset              # return this value to calculate the offset
		
def yoffsets(data_files):
	
	ymean = []
	for i in data_files:
		xyz_offsets = calc_mean(i)
		ymean.append(xyz_offsets[1])
		
	total_yoffset = np.mean(ymean)
	
	return total_yoffset

def zoffsets(data_files):
	
	zmean = []
	for i in data_files:
		xyz_offsets = calc_mean(i)
		zmean.append(xyz_offsets[2])
		
	total_zoffset = np.mean(zmean)
	
	return total_zoffset		
	

# returns list of all files in that directory
files_zpos = glob.glob('/home/fissellab/BVEX/accelerometer/accel_data/+z/*.csv')
files_zneg = glob.glob('/home/fissellab/BVEX/accelerometer/accel_data/-z/*.csv')

files_xpos = glob.glob('/home/fissellab/BVEX/accelerometer/accel_data/+x/*.csv')
files_xneg = glob.glob('/home/fissellab/BVEX/accelerometer/accel_data/-x/*.csv')

files_ypos = glob.glob('/home/fissellab/BVEX/accelerometer/accel_data/+y/*.csv')
files_yneg = glob.glob('/home/fissellab/BVEX/accelerometer/accel_data/-y/*.csv')


# add pos and neg g values together and divide by 2
zpos = zoffsets(files_zpos)
zneg = zoffsets(files_zneg)
zoffset = (zpos + zneg)/2
print("\n z offset: {:.12f}".format(zoffset))  # this would be the value to subtract from accel to remove bias

ypos = yoffsets(files_ypos)
yneg = yoffsets(files_yneg)
yoffset = (ypos + yneg)/2
print("\n y offset: {:.12f}".format(yoffset))

xpos = xoffsets(files_xpos)
xneg = xoffsets(files_xneg)
xoffset = (xpos + xneg) / 2
print("\n x offset: {:.12f}".format(xoffset))

