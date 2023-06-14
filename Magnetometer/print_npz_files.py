import numpy as np
import matplotlib.pyplot as plt

mag_npz = np.load('/home/bvextp1/Magnetometer/Mag2_outside.npz')
imu_npz = np.load('/home/bvextp1/IMU/IMU_outside.npz', allow_pickle=True)

mag_headers = mag_npz['arr_0']
mag_data = mag_npz['arr_1']

imu_headers = imu_npz['arr_0']
imu_data = imu_npz['arr_1']
print(mag_headers)
print(mag_data)
print(imu_headers)
print(imu_data[:,4])
print(imu_data[:,5])
print(imu_data[:,6])
