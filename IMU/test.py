import numpy as np

f = '/home/fissellab/BVEX/IMU/test.csv'
data = np.loadtxt(f, delimiter=',', skiprows=2)

time = data[:,7]
t0 = time[0]
tend = time[-1]

seconds = (tend - t0) * 1e-9
print(len(data) / seconds)  # 62 Hz
