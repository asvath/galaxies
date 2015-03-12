#calculates the density of a galaxy, where r is the half light radius in kpc
import numpy as np
def gal_density(sigma,r)
	G=6.6784*10**-11
	kpc=3.0856*10**19
	radius=r*kpc
	denisty=(9*sigma**2)/(20*np.pi*radius*G)
	print density
	return density


