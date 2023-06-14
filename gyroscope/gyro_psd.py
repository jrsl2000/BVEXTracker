import numpy as np
import matplotlib.pyplot as plt

def psd_matplot(x, y, z):
	# subtract the mean from the data
	xoff = x - np.mean(x)
	yoff = y - np.mean(y)
	zoff = z - np.mean(z)
	
	sampleRate = len(x) / 60
	
	fig, ax = plt.subplots(2, 2, figsize=(8,6), dpi=105)
	plt.rcParams.update({'font.size':12})
	
	fig.suptitle('Gyro PSD using matplotlib.psd, Fs={:.0f} Hz'.format(sampleRate))
	
	ax[0,0].psd(xoff, Fs=sampleRate)
	ax[0,0].psd(yoff, Fs=sampleRate)
	ax[0,0].psd(zoff, Fs=sampleRate)
	
	ax[0,1].psd(xoff, Fs=sampleRate,label='X axis')
	ax[0,1].legend()
	
	ax[1,0].psd(yoff, Fs=sampleRate, label='Y axis')
	ax[1,0].legend()
	
	ax[1,1].psd(zoff, Fs=sampleRate, label='Z axis')
	ax[1,1].legend()
	
	plt.show()
	
	
def psd_fromfft(x, y, z):
	# subtract the mean
	xoff = x - np.mean(x)
	yoff = y - np.mean(y)
	zoff = z - np.mean(z)
	
	N = len(x)
	sampleRate = N / 60  # sampled for 1 min
	nyquist = sampleRate / 2
	 

	freq = sampleRate * np.arange((N/2)) / N

	xfft = np.fft.fft(xoff)[0:int(N/2)] / N     # half the spectrum
	yfft = np.fft.fft(yoff)[0:int(N/2)] / N
	zfft = np.fft.fft(zoff)[0:int(N/2)] / N
	
	xfft[1:] = 2*xfft[1:] 
	yfft[1:] = 2*yfft[1:]
	zfft[1:] = 2*zfft[1:]

	xpsd = np.abs(xfft)**2
	ypsd = np.abs(yfft)**2
	zpsd = np.abs(zfft)**2
	
	threshold = 0.0004
	psd_idx = xpsd > threshold
	psd_idy = ypsd > threshold
	psd_idz = zpsd > threshold
	xpsd_clean = xpsd * psd_idx
	ypsd_clean = ypsd * psd_idy
	zpsd_clean = zpsd * psd_idz
	
	fig, ax = plt.subplots(3, 1, figsize=(8,6), dpi=100)
	plt.rcParams.update({'font.size':12})
	
	fig.suptitle('Gyro PSD using np.fft, Fs={:.0f} Hz'.format(sampleRate), fontsize=16)

	ax[0].plot(freq[:-1], xpsd, label='X axis, noisy')
	#ax[0].plot(freq[:-1], xpsd_clean, label='filtered noise')
	ax[0].legend()
	ax[0].set_xscale('log')
	ax[0].set_yscale('log')
	ax[0].set_ylim([10**-9, 10**-3])
	
	ax[1].plot(freq[:-1], ypsd, label='Y axis')
	#ax[1].plot(freq[:-1], ypsd_clean, label='filtered noise')
	ax[1].legend()
	ax[1].set_xscale('log')
	ax[1].set_yscale('log')
	ax[1].set_ylim([10**-9, 10**-3])
	
	ax[2].plot(freq[:-1], zpsd, label='Z axis')
	#ax[2].plot(freq[:-1], zpsd_clean, label='filtered noise')
	ax[2].legend()
	ax[2].set_xscale('log')
	ax[2].set_yscale('log')
	ax[2].set_ylim([10**-9, 10**-3])
	
	plt.show()
	
	
# read data from file
f = '/home/fissellab/BVEX/gyroscope/gyrodata.csv'
gyro_data = np.loadtxt(f, delimiter=',', usecols=(0,1,2))

xdata = gyro_data[:,0]
ydata = gyro_data[:,1]
zdata = gyro_data[:,2]

#psd_matplot(xdata,ydata,zdata)
psd_fromfft(xdata, ydata, zdata)
