import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

### Functions
def plot_hist(latdata, londata, altdata, speeddata, vx, vy, vz):
	fig, ax = plt.subplots(2,4, figsize=(12,8), dpi=100)
	plt.rcParams.update({'font.size':11})
	
	fig.suptitle('GPS 20 Hz, 5 minutes', fontsize=16)
	
	ax[0,0].hist(latdata)
	ax[0,0].set_title('Latitude (deg)')
	ax[0,0].xaxis.set_major_formatter(mtick.FormatStrFormatter('%.5f'))
	
	ax[0,1].hist(londata)
	ax[0,1].set_title('Longitude (deg)')
	#ax[0,1].set_xticks([-76.49716, -76.49714, -76.49712])
	ax[0,1].xaxis.set_major_formatter(mtick.FormatStrFormatter('%.5f'))
	
	ax[0,2].hist(altdata)
	ax[0,2].set_title('Altitude (m)')
	
	ax[0,3].hist(speeddata)
	ax[0,3].set_title('Speed (m/s)')
	
	ax[1,0].hist(vx)
	ax[1,0].set_title('vx')
	
	ax[1,1].hist(vy)
	ax[1,1].set_title('vy')
	
	ax[1,2].hist(vz)
	ax[1,2].set_title('vz')
	
	plt.tight_layout()
	
	plt.show()
	
def psd_fromfft(latdata, londata, altdata, speeddata):
	# subtract the mean
	latoff = latdata - np.mean(latdata)
	lonoff = londata - np.mean(londata)
	altoff = altdata - np.mean(altdata)
	speedoff = speeddata - np.mean(speeddata)
	
	N = len(latdata)
	sampleRate = N / 60  # sampled for 1 min
	nyquist = sampleRate / 2

	freq = sampleRate * np.arange((N/2)) / N

	latfft = np.fft.fft(latoff)[0:int(N/2)] / N     # half the spectrum
	lonfft = np.fft.fft(lonoff)[0:int(N/2)] / N
	altfft = np.fft.fft(altoff)[0:int(N/2)] / N
	spfft = np.fft.fft(speedoff)[0:int(N/2)] / N
	
	latfft[1:] = 2*latfft[1:] 
	lonfft[1:] = 2*lonfft[1:]
	altfft[1:] = 2*altfft[1:]
	spfft[1:] = 2*spfft[1:]

	latpsd = np.abs(latfft)**2
	lonpsd = np.abs(lonfft)**2
	altpsd = np.abs(altfft)**2
	sppsd = np.abs(spfft)**2
	
	fig, ax = plt.subplots(2, 2, figsize=(8,8), dpi=100)
	plt.rcParams.update({'font.size':12})
	
	fig.suptitle('PSD using np.fft, 20 Hz, 1min', fontsize=16)

	ax[0,0].plot(freq, latpsd)
	#ax[0,0].psd(latoff, Fs=sampleRate)
	ax[0,0].set_title('Latitude')
	ax[0,0].set_xscale('log')
	ax[0,0].set_yscale('log')
	ax[0,0].set_ylim([10**-17, 10**-9])
	ax[0,0].set_xticks([10**-2, 10**-1, 10**0, 10**1])
	ax[0,0].set_xlabel('Frequency (Hz)')
	ax[0,0].set_ylabel('')
	#ax[0,0].set_xlim([-0.1, 0.1])

	ax[0,1].plot(freq, lonpsd)
	ax[0,1].set_title('Longitude')
	ax[0,1].set_xscale('log')
	ax[0,1].set_yscale('log')
	ax[0,1].set_ylim([10**-15, 10**-8])
	ax[0,1].set_xticks([10**-2, 10**-1, 10**0, 10**1])
	ax[0,1].set_xlabel('Frequency (Hz)')
	ax[0,1].set_ylabel('')


	ax[1,0].plot(freq, altpsd)
	ax[1,0].set_title('Altitude')
	ax[1,0].set_xscale('log')
	ax[1,0].set_yscale('log')
	ax[1,0].set_ylim([10**-6, 10**2])
	ax[1,0].set_xticks([10**-2, 10**-1, 10**0, 10**1])
	ax[1,0].set_xlabel('Frequency (Hz)')
	ax[1,0].set_ylabel('')

	ax[1,1].plot(freq, sppsd)
	ax[1,1].set_title('Speed')
	ax[1,1].set_xscale('log')
	ax[1,1].set_yscale('log')
	ax[1,1].set_ylim([10**-10, 10**-2])
	ax[1,1].set_xticks([10**-2, 10**-1, 10**0, 10**1])
	ax[1,1].set_xlabel('Frequency (Hz)')
	ax[1,1].set_ylabel('')

	plt.tight_layout()

	plt.show()
	


### Read data from file
filename = '/home/fissellab/BVEX/GPS/gpsdata_20Hz_5min.csv'
gps_data = np.loadtxt(filename, delimiter=',')
	
latitude = gps_data[:,0]   # degrees
longitude = gps_data[:,1]  # degrees
altitude = gps_data[:,2]   # meters
speed = gps_data[:,3]      # m/s^2
ecefvx = gps_data[:,4]
ecefvy = gps_data[:,5]
ecefvz = gps_data[:,6]
timestamp = gps_data[:,-1]


#print('Latitude std: {:.4e}'.format(latstd))
#print('Longitude std: {:.4e}'.format(lonstd))
#print('Altitude std: {:.4e}'.format(altstd))
#print('Speed std: {:.4e}'.format(speedstd))

plot_hist(latitude, longitude, altitude, speed, ecefvx, ecefvy, ecefvz)
#psd_fromfft(latitude, longitude, altitude, speed)

