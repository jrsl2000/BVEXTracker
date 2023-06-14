import numpy as np
import matplotlib.pyplot as plt

data_file = np.load('/home/bvextp1/IMU/IMU_outside.npz')
#print(data_file.files)
data_array = data_file['arr_1'] # select only data, exclude timestamp and header

# seperate time,x,y,z data
timestamp = data_array[:,0]
data_x = data_array[:,4] 
data_y = data_array[:,5]
data_z = data_array[:,6]

sampling_rate = 155
N = len(data_x) # number of data points

time = np.linspace(0, 60, len(data_x)) # create time array for x axis

##### Magnetic Field Data ######
fig, axs = plt.subplots(2)
axs[0].plot(time, data_x, label='X', color='darkorange')
axs[0].plot(time, data_y, label='Y', color='seagreen')
axs[0].plot(time, data_z, label ='Z', color='royalblue')
axs[0].set_xlabel('Time (s)')
axs[0].set_ylabel('Magnetic Field (uT)')
axs[0].legend()

axs[1].hist(data_x, bins=20, color='darkorange')
axs[1].hist(data_y, bins=20, color='seagreen')
axs[1].hist(data_z, bins=20, color='royalblue')
axs[1].set_xlabel('Magnetic Field (uT)')
axs[1].set_ylabel('Number of Bins')

##### FFT #######
x = data_x - np.mean(data_x)
fft_x = np.abs(np.fft.fft(x))

y = data_y - np.mean(data_y)
fft_y = np.abs(np.fft.fft(y))

z = data_z - np.mean(data_z)
fft_z = np.abs(np.fft.fft(z))

freq = sampling_rate*np.arange((N/2.))/N

fig1, axs1 = plt.subplots(3)
axs1[0].plot(freq, fft_x[0:len(freq)], label="X", color='darkorange')
axs1[0].set_xscale('log')
axs1[0].set_yscale('log')
axs1[0].set_xlabel('Frequency (Hz)')
axs1[0].set_ylabel('PSD')
axs1[0].set_ylim([10**-1,10**6])
axs1[0].legend()

axs1[1].plot(freq, fft_y[0:len(freq)], label="Y", color='seagreen')
axs1[1].set_xscale('log')
axs1[1].set_yscale('log')
axs1[1].set_xlabel('Frequncy (Hz)')
axs1[1].set_ylabel('PSD')
axs1[1].set_ylim([10**-1,10**6])
axs1[1].legend()

axs1[2].plot(freq, fft_z[0:len(freq)], label="Z", color='royalblue')
axs1[2].set_xscale('log')
axs1[2].set_yscale('log')
axs1[2].set_xlabel('Frequency (Hz)')
axs1[2].set_ylabel('PSD')
axs1[2].set_ylim([10**-1,10**6])
axs1[2].legend()

plt.show()
