#finds the X!
import numpy as np
def xval(density,mass,radius,delta):
	denisty=density*10**-20
	G=6.6784*10**-11
	kpc=3.0856*10**19
	r=radius*kpc
	sun=(1.989*10**30)*10**9
	m=mass*sun
	glob=4*np.pi*G*density*(1+delta)
	glob2=(G*m*delta)/r**2
	x=glob2/glob
	print x
	return x



if __name__ == "__main__":
    import sys
    xval(float(sys.argv[1]),float(sys.argv[2]),float(sys.argv[3]),float(sys.argv[4]))

	
