from pydns import derivatives as der
import matplotlib.pyplot as plt
from math import pi
import numpy as np
import unittest

class TestDerivatives(unittest.TestCase):

  plotresults = 0

  def setUp(self):
    der.nn = (33,1,1)
    der.ll = [2.*pi,2.*pi,2.*pi]
    der.dd = [der.ll[i]/der.nn[i] for i in range(0,3)]
    der.setup()
    self.x = np.linspace(0,der.ll[0],der.nn[0])
    self.y = np.zeros(der.nn)
    self.y[:,0,0] = np.cos(self.x)
    self.dy = np.zeros(der.nn)
    self.dy[:,0,0] = -np.sin(self.x)

  def test_x_shape(self):
    # make sure the shape of x is correct. More a test of the tests
    self.assertEqual(np.shape(self.y),der.nn)

  def test_1d_derivative_in_x(self):
    result = der.dxi(self.y,axis=0,order=1)

    if self.plotresults == 1:
      plt.plot(np.arange(der.nn[0]),result[:,0,0],np.arange(der.nn[0]),self.dy[:,0,0])
      plt.title('Derivative test: analytical vs approximate solution')
      plt.show()

    print np.sum((result-self.dy)**2)
    self.assertTrue(np.sum((result - self.dy)**2) < 0.05)
