import numpy as np
from math import pi
from constants import nn,ll,dd

# Derivatives: logic related to calculating derivatives
# What this module assumes:
# -  Once setup, the field variables will always have the same size
# - 


### ATTRIBUTES ###
# xk: wave numbers for each axis
# setup: is the module properly setup?
xk = []


### FUNCTIONS ###
def setup():
  global xk
  # Setup the wave numbers for derivatives

  xk = np.zeros([3,max(nn)],dtype=np.complex)
  for i in range(0,3):
    xk[i,0:nn[i]] = 2.*np.pi*1.*1j*np.fft.fftfreq(nn[i],dd[i])


  # TODO calculate xk for each direction

def dxi(A,axis=0,order=1):
  global xk
  # Calculate the derivative of the field with respect to the given axis
  #  d/dx: axis 0
  #  d/dy: axis 1
  #  d/dz: axis 2

  # Take an fft of the A
  fftA = np.fft.fft(A,axis=axis)

  # multiply each wave number by the derivative weight
  if axis==0:
    for iy in range(0,nn[1]):
      for iz in range(0,nn[2]):
        fftA[:,iy,iz] = fftA[:,iy,iz]*(xk[0,0:nn[0]]**order)
  elif axis==1:
    for ix in range(0,nn[0]):
      for iz in range(0,nn[2]):
        fftA[ix,:,iz] = 2.*np.pi*fftA[ix,:,iz]*xk[1,0:nn[1]]**order
  elif axis==2:
    for ix in range(0,nn[0]):
      for iy in range(0,nn[1]):
        fftA[ix,iy,:] = 2.*np.pi*fftA[ix,iy,:]*xk[2,0:nn[2]]**order

  return np.real(np.fft.ifft(fftA,axis=axis))

def dx2i(A,axis=0):
  # Calculate the second derivative of the field with respect to the given axis
  #  d^2/dx^2: axis 0
  #  d^2/dy^2: axis 1
  #  d^2/dz^2: axis 2

  print 'not yet implimented'
  return -1

