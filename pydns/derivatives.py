import numpy as np
from constants import nn,ll,dd

# Derivatives: logic related to calculating derivatives
# What this module assumes:
# -  Once setup, the field variables will always have the same size
# - 


### ATTRIBUTES ###
# xk: wave numbers for each axis
# setup: is the module properly setup?
xk = []
setup = 0


### FUNCTIONS ###
def setup():
  # Setup the wave numbers for derivatives
  for i in range(0,3):
    for j in range(0,nn(i)):
      xk(i,j) = float(j-1)*2*np.pi/ll(i)/nn(i)

  # TODO calculate xk for each direction

def dxi(field,axis=0):
  # Calculate the derivative of the field with respect to the given axis
  #  d/dx: axis 0
  #  d/dy: axis 1
  #  d/dz: axis 2
  derivative = field
  return derivative

def dx2i(field,axis=0):
  # Calculate the second derivative of the field with respect to the given axis
  #  d^2/dx^2: axis 0
  #  d^2/dy^2: axis 1
  #  d^2/dz^2: axis 2

