import numpy as np
from numpy import pi

# nn: Number of grid points
# ll: Physical size of domain (meters)
# dt_max: The maximum time step for your problem (seconds)
# rho: Density of the fluid (kg/m^3)
# nu: Kinematic Viscosity (m^2/s)

nn = np.array([256,256,256])
ll = np.array([pi, pi, pi])
dd = [ll[i]/nn[i] for i in range(0,3)]
dt_max = 0.5
rho = 1.839 #~300K air
nu = .00001568 #~300K air


#Velocity Boundary Conditions
#top is zero flux in Z direction
#bottom is no slip
#sides are periodic

x1 = 'periodic'
x2 = 'periodic'
y1 = 'periodic'
y2 = 'periodic'
z1 = 'noslip'
z2 = 'nogradient'

velBC=[x1, x2, y1, y2, z1, z2]

#Pressure Boundary Conditions

x1 = 'periodic'
x2 = 'periodic'
y1 = 'periodic'
y2 = 'periodic'
z1 = ''
z2 = ''

pressureBC=[x1, x2, y1, y2, z1, z2]
