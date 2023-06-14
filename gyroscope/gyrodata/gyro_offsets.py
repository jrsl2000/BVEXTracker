import numpy as np
import glob

# load files then calculate the mean for each axis
def calc_mean(filename):
	data = np.loadtxt(filename, delimiter=',')
	
	x = data[:,0]
	y = data[:,1]
	z = data[:,2]
	
	xmean = np.mean(x)
	ymean = np.mean(y)
	zmean = np.mean(z)
	
	mean_list = [xmean, ymean, zmean]
	return mean_list

# returns list of all files in that directory
files = glob.glob('/home/fissellab/BVEX/gyroscope/gyrodata/*.csv')

xmean = []
ymean = []
zmean = []
for i in files:
	xmean.append(calc_mean(i)[0])
	ymean.append(calc_mean(i)[1])
	zmean.append(calc_mean(i)[2])
	
xoffset = np.mean(xmean)
yoffset = np.mean(ymean)
zoffset = np.mean(zmean)

# subtract the mean values 
print("{:.12f}".format(xoffset))
print("{:.12f}".format(yoffset))
print("{:.12f}".format(zoffset))
