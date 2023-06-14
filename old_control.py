import time
import threading


file1_path = '/home/fissellab/BVEX/accelerometer/adxl355-pi-master/record_spi.py'
file2_path = '/home/fissellab/BVEX/GPS/GPSD/gpsd_data.py'
file3_path = '/home/fissellab/BVEX/gyroscope/gyro_timer.py'
file4_path = '/home/fissellab/BVEX/IMU/IMU.py'
file5_path = '/home/fissellab/BVEX/Magnetometer/Magnetometer.py'

file1_process = subprocess.Popen(['python', file1_path])
file2_process = subprocess.Popen(['python', file2_path])
file3_process = subprocess.Popen(['python', file3_path])
file4_process = subprocess.Popen(['python', file4_path])
file5_process = subprocess.Popen(['python', file5_path])

file1_process.wait()
file2_process.wait()
file3_process.wait()
file4_process.wait()
file5_process.wait()

print("All files ran")
