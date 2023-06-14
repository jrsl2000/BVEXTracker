import numpy as np

f = '/home/fissellab/BVEX/gyroscope/gyro_test.csv'
data = np.loadtxt(f, delimiter=',')

x = data[:,0]
y = data[:,1]
z = data[:,2]
time = data[:,3]

t0 = time[0]
tend = time[-1]

difftime = (tend - t0) * 1e-9
print(difftime) 
print(len(x) / difftime)

print('{:.8f}'.format(np.mean(x)))
print('{:.8f}'.format(np.mean(y)))
print('{:.8f}'.format(np.mean(z)))
