#calculates the density of a galaxy, where r is the half light radius in kpc
import numpy as np
def gal_density(sigma,r):
	G=6.6784*10**(-11)
	kpc=3.0856*10**19
	radius=r*kpc
	sigma=sigma*1000
	density=(5*sigma**2)/(4*np.pi*(radius**2)*G)
	#density=(3*sigma**2)/(4*np.pi*(radius**2)*G)
	#print density
	sun=density/(1.98*10**30)
	mm=3.24*10**(-17)
	den=sun/(mm**3)
	print sigma
	print den

	#return density





if __name__ == "__main__":
    import sys
    gal_density(float(sys.argv[1]),float(sys.argv[2]))

