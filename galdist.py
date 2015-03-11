#calculates the distance between two astro objects 
import numpy as np
def galdist(ra1,dec1,r1,ra2,dec2,r2):
	x1=r1*np.cos(np.radians(ra1))*np.cos(np.radians(dec1))
	y1=r1*np.sin(np.radians(ra1))*np.cos(np.radians(dec1))
	z1=r1*np.sin(np.radians(dec1))

	x2=r2*np.cos(np.radians(ra2))*np.cos(np.radians(dec2))
	y2=r2*np.sin(np.radians(ra2))*np.cos(np.radians(dec2))
	z2=r2*np.sin(np.radians(dec2))

	x=x2-x1
	y=y2-y1
	z=z2-z1
	dist=np.sqrt(x**2+y**2+z**2)

	print dist
	return dist


if __name__ == "__main__":
    import sys
    galdist(float(sys.argv[1]),float(sys.argv[2]),float(sys.argv[3]),float(sys.argv[4]),float(sys.argv[5]),float(sys.argv[6]))
