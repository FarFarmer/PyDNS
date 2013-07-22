import numpy as np
from constants import nn, ll, dd, dudz


#logic is to generate a random nn[0] x nn[1] x nn[2] field, take gradients
#in the horizontal directions and set velocities equal to the value of the
#gradient in the perpendicular direction, making for a divergence free
#field.  We will set the initial vertical velocity to be 0.

#underlying velocity profiles can then be added.

## Create initial fields from a normal distribution##

Q=np.random.randn(nn[0],nn[1],nn[2])
Qx,Qy,Qz=np.gradient(q)

U=Qy[:]
V=-Qx[:]

# add underlying shear profile
U=U+U[]





