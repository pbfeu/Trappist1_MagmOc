import numpy as np

# read data
data = np.loadtxt("GJ1132.GJ1132b.forward")

time        = data[:,0] # time (yr)
Press_O     = data[:,9] # partial pressure oxygen in atmosphere (bar)

n_time = len(time)

print('Solidification Time           = ',time[n_time-1]*1e-6,  ' Myr')
print('Oxygen pressure in atmosphere = ',Press_O[n_time-1],    ' bar')
