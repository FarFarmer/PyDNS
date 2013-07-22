import numpy as np
from constants import velBC, pressureBC
from field import U, V, W
from pressure import P

# Module takes velocity or pressure fields and applies BC's
# Assumes fields are 256x256x256 ordered x,y,z


### FUNCTIONS ###
def imposeVelBC(U,V,W,velBC):
	Umod=U[:]
	Vmod=V[:]
	Wmod=W[:]

	for i in range(0,5):
		
		#Periodic Boundary Conditions
		if velBC[i] == 'periodic':
			
			if i == 0:
				Umod[-1,:,:]=Umod[0,:,:]
				Vmod[-1,:,:]=Vmod[0,:,:]
				Wmod[-1,:,:]=Wmod[0,:,:]
			elif i == 2:
				Umod[:,-1,:]=Umod[:,0,:]
				Vmod[:,-1,:]=Vmod[:,0,:]
				Wmod[:,-1,:]=Wmod[:,0,:]
			elif i == 4:
				Umod[:,:,-1]=Umod[:,:,0]
				Vmod[:,:,-1]=Vmod[:,:,0]
				Wmod[:,:,-1]=Wmod[:,:,0]

		#No slip conditions
		elif velBC[i] == 'noslip':
			if i == 0:
				Umod[0,:,:]=0
				Vmod[0,:,:]=0
				Wmod[0,:,:]=0
			elif i == 1:
				Umod[-1,:,:]=0
				Vmod[-1,:,:]=0
				Wmod[-1,:,:]=0
			elif i == 2:
				Umod[:,0,:]=0
				Vmod[:,0,:]=0
				Wmod[:,0,:]=0
			elif i == 3:
				Umod[:,-1,:]=0
				Vmod[:,-1,:]=0
				Wmod[:,-1,:]=0
			elif i == 4:
				Umod[:,:,0]=0
				Vmod[:,:,0]=0
				Wmod[:,:,0]=0
			elif i == 5:
				Umod[:,:,-1]=0
				Vmod[:,:,-1]=0
				Wmod[:,:,-1]=0

		#No flux conditions
		elif velBC[i] == 'nogradient':
			if i == 0:
				Umod[0,:,:]=Umod[1,:,:]
				Vmod[0,:,:]=Vmod[1,:,:]
				Wmod[0,:,:]=Wmod[1,:,:]
			elif i == 1:
				Umod[-1,:,:]=Umod[-2,:,:]
				Vmod[-1,:,:]=Vmod[-2,:,:]
				Wmod[-1,:,:]=Wmod[-2,:,:]
			elif i == 2:
				Umod[:,0,:]=Umod[:,1,:]
				Vmod[:,0,:]=Vmod[:,1,:]
				Wmod[:,0,:]=Wmod[:,1,:]
			elif i == 3:
				Umod[:,-1,:]=Umod[:,-2,:]
				Vmod[:,-1,:]=Vmod[:,-2,:]
				Wmod[:,-1,:]=Wmod[:,-2,:]
			elif i == 4:
				Umod[:,:,0]=Umod[:,:,1]
				Vmod[:,:,0]=Vmod[:,:,1]
				Wmod[:,:,0]=Wmod[:,:,1]
			elif i == 5:
				Umod[:,:,-1]=Umod[:,:,-2]
				Vmod[:,:,-1]=Vmod[:,:,-2]
				Wmod[:,:,-1]=Wmod[:,:,-2]

	return Umod, Vmod, Wmod

def imposePressureBC(P,pressureBC):
	Pmod=P[:]

	for i in range(0,5):
		
		#Periodic Boundary Conditions
		if pressureBC[i] == 'periodic':
			
			if i == 0:
				Pmod[-1,:,:] = Pmod[0,:,:]
				
			elif i == 2:
				Pmod[:,-1,:] = Pmod[:,0,:]

			elif i == 4:
				Pmod[:,:,-1] = Pmod[:,:,0]

		#No gradient BC
		elif pressureBC[i] == 'nogradient':

			if i == 0:
				Pmod[0,:,:] = Pmod[1,:,:]

			elif i == 1:
				Pmod[-1,:,:] = Pmod[-2,:,:]

			elif i == 2:
				Pmod[:,0,:]=Pmod[:,1,:]

			elif i == 3:
				Pmod[:,-1,:]=Pmod[:,-2,:]
			
			elif i == 4:
				Pmod[:,:,0]=Pmod[:,:,1]
				
			elif i == 5:
				Pmod[:,:,-1]=Pmod[:,:,-2]

	return Pmod
	
				



