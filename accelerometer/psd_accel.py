import numpy as np
import matplotlib.pyplot as plt

def psd_fromfft(x, y, z):
	# subtract the mean
	xmean = np.mean(x)
	ymean = np.mean(y)
	zmean = np.mean(z)

	xoff = x-xmean
	yoff = y-ymean 
	zoff = z-zmean
	
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
	
	fig, ax = plt.subplots(3, 1, figsize=(8,6), dpi=100)
	plt.rcParams.update({'font.size':12})
	
	fig.suptitle('Accel PSD using np.fft, 1kHz, 1min', fontsize=16)

	ax[0].plot(freq, xfft)
	#ax[0].psd(latoff, Fs=sampleRate)
	ax[0].set_title('X axis')
	ax[0].set_xscale('log')
	ax[0].set_yscale('log')
	ax[0].set_ylim([10**-13, 10**-4])
	#ax[0].set_xticks([10**-2, 10**-1, 10**0])
	ax[0].set_xlabel('Frequency (Hz)')
	ax[0].set_ylabel('')
	#ax[0].set_xlim([-0.1, 0.1])

	ax[1].plot(freq, ypsd)
	ax[1].set_title('Y axis')
	ax[1].set_xscale('log')
	ax[1].set_yscale('log')
	ax[1].set_ylim([10**-13, 10**-4])
	#ax[1].set_xticks([10**-2, 10**-1, 10**0])
	ax[1].set_xlabel('Frequency (Hz)')
	ax[1].set_ylabel('')


	ax[2].plot(freq, zpsd)
	ax[2].set_title('Z axis')
	ax[2].set_xscale('log')
	ax[2].set_yscale('log')
	ax[2].set_ylim([10**-13, 10**-4])
	#ax[2].set_xticks([10**-2, 10**-1, 10**0])
	ax[2].set_xlabel('Frequency (Hz)')
	ax[2].set_ylabel('')

	plt.tight_layout()

	plt.show()
	
def matplotlibpsd(x, y, z):
	# subtract the mean
	xmean = np.mean(x)
	ymean = np.mean(y)
	zmean = np.mean(z)

	xoff = x-xmean
	yoff = y-ymean 
	zoff = z-zmean
	
	N = len(x)
	sampleRate = N / 60  # sampled for 1 min
	nyquist = sampleRate / 2
	
	fig, ax = plt.subplots(3, 1, figsize=(8,6), dpi=100)
	plt.rcParams.update({'font.size':12})
	
	fig.suptitle('Accel PSD using matplotlib, 1kHz, 1min', fontsize=16)

	ax[0].psd(xoff, Fs=sampleRate)
	ax[0].set_title('X axis')

	ax[1].psd(yoff, Fs=sampleRate)
	ax[1].set_title('Y axis')


	ax[2].psd(zoff, Fs=sampleRate)
	ax[2].set_title('Z axis')

	plt.tight_layout()

	plt.show()

### Read the data
data = np.loadtxt('/home/fissellab/BVEX/accelerometer/output.csv', delimiter=',')

xdata = data[:,0]
ydata = data[:,1]
zdata = data[:,2]
t = data[0]

print(t)

# for some reason when taking the mean it's returning nan even though there are no missing values
#xdata_clean = xdata[~np.isnan(xdata)]
#ydata_clean = ydata[~np.isnan(ydata)]
#zdata_clean = zdata[~np.isnan(zdata)]

#plt.plot(xdata_clean)
#plt.show()

#psd_fromfft(xdata, ydata, zdata)
#matplotlibpsd(xdata_clean, ydata_clean, zdata_clean)


