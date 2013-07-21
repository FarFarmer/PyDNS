from numpy import pi

# nn: Number of grid points
# ll: Physical size of grid (meters)
# dt_max: The maximum time step for your problem (seconds)
# rho: Density of the fluid (kg/m^3)
# nu: Kinematic Viscosity (m^2/s)

nn = (256,256,256)
ll = (pi, pi, pi)
dd = [ll[i]/nn[i] for i in range(0,3)]
dt_max = 0.5
rho = 1.839
nu = .00001568
