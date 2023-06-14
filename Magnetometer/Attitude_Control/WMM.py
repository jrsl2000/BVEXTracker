from ahrs.utils import WMM
import datetime
import numpy as np
import matplotlib.pyplot as plt

wmm = WMM(latitude=44.233334 , longitude=-76.5 , height=0.093, date=datetime.date(2023, 6, 9)) # Set parameters for Kingston

X = (wmm.X)*0.001
Y = (wmm.Y)*0.001
Z = (wmm.Z)*0.001
H = (wmm.H)*0.001
F = (wmm.F)*0.001

# Print magnetic model values
print("North Component X: {:.2f} (uT)".format(X))
print("East Component Y: {:.2f} (uT)".format(Y))
print("Vertical Component Z: {:.2f} (uT)".format(Z))
print("Horizontal Intensity H: {:.2f} (uT)".format(H))
print("Total Intensity F: {:.2f} (uT)".format(F))
print("Inclination Angle I: {:.2f} (deg)".format(wmm.I))
print("Declination Angle D: {:.2f} (deg)".format(wmm.D))


data_file = np.load('/home/bvextp1/Magnetometer/Mag2_outside.npz')
#print(data_file.files)
data_array = data_file['arr_1'] # select only data, exclude timestamp and header

# seperate time,x,y,z data
timestamp = data_array[:,0]
data_x = data_array[:,1]
data_y = data_array[:,2]
data_z = data_array[:,3]

time = np.linspace(0, 60, len(data_x)) # create time array for x axis

##### Magnetic Field Magnetometer ######
#plt.plot(time, data_x, label='X Mag', color='darkorange')
#plt.plot(time, data_y, label='Y Mag', color='seagreen')
#plt.plot(time, data_z, label ='Z Mag', color='royalblue')
plt.axhline(y = X, color = 'r', linestyle = '-', label = 'X')
plt.axhline(y = Y, color = 'g', linestyle = '-', label = 'Y')
plt.axhline(y = Z, color = 'b', linestyle = '-', label = 'Z')
plt.xlabel('Time (s)')
plt.ylabel('Magnetic Field (uT)')
plt.legend()

data_file2 = np.load('/home/bvextp1/IMU/IMU_outside.npz')
#print(data_file.files)
data_array2 = data_file2['arr_1'] # select only data, exclude timestamp and header

# seperate time,x,y,z data
timestamp = data_array2[:,0]
imu_x = data_array2[:,4] 
imu_y = data_array2[:,5]
imu_z = data_array2[:,6]

imux = []
imuy =[]
imuz = []
for i in range(0, len(imu_x)):
	imux.append(imu_x[i])
	imuy.append(imu_y[i])
	imuz.append(imu_z[i])


time2 = np.linspace(0, 60, len(imux)) # create time array for x axis

##### Magnetic Field IMU ######
plt.plot(time2, imux, label='X imu', color='orange')
plt.plot(time2, imuy, label='Y imu', color='green')
plt.plot(time2, imuz, label ='Z imu', color='blue')
plt.legend()

plt.show()
