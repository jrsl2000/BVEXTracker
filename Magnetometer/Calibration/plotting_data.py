import numpy as np
import matplotlib.pyplot as plt

data_file = np.load('/home/bvextp1/IMU/IMU.npz')
headers = data_file['arr_0']
data = data_file['arr_1']

x = data[:,4]
y = data[:,5]
z = data[:,6]
'''
# 2D magnetic field
fig, ax = plt.subplots(1,1)
ax.set_aspect(1)
ax.scatter(x, y, color = 'orange', label = 'XY')
ax.scatter(y, z, color = 'seagreen', label = 'YZ')
ax.scatter(z, y, color = 'royalblue', label = 'ZX')
#ax.set_title('{}'.format(timestamp))
ax.legend()'''

# Magnetic field over time
t = np.linspace(0, 120, len(x)) # create time array for x axis
fig1, ax1 = plt.subplots(1)
ax1.plot(t, x, color = 'orange', label = 'X')
ax1.plot(t, y, color = 'seagreen', label = 'Y')
ax1.plot(t, z, color = 'royalblue', label = 'Z')
#ax1.set_title('{}'.format(timestamp))
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('')
ax1.legend()

'''# 3D magnetic field with unit sphere
fig2 = plt.figure()
ax2 = fig2.add_subplot(111, projection='3d')
ax2.scatter(x, y, z, s=1, color='r')
ax2.set_xlabel('X (uT)')
ax2.set_ylabel('Y (uT)')
ax2.set_zlabel('Z (uT)')

u = np.linspace(0,2*np.pi, 100)
v = np.linspace(0,np.pi,100)
x = np.outer(np.cos(u), np.sin(v))
y = np.outer(np.sin(u), np.sin(v))
z = np.outer(np.ones(np.size(u)), np.cos(v))
ax2.plot_wireframe(x,y,z, rstride=10, cstride=10, alpha=0.5)
ax2.plot_surface(x,y,z,alpha=0.3,color='b')'''

plt.show()
