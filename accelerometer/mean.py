import numpy as np

f = '/home/fissellab/BVEX/accelerometer/output.npz'
npzfile = np.load(f)
print(npzfile['arr_0'])
print(npzfile['arr_1'])
print(npzfile['arr_2'])
print(npzfile['arr_3'])
