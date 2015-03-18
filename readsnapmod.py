import numpy as np
import matplotlib.pyplot as plt

def readsnap(filename,a):
	with open(filename,"r") as f:
    		np.fromfile(f, dtype='uint32',count=1)
    		npart = np.fromfile(f, dtype='uint32',count=6) 
    		mass = np.fromfile(f, dtype='double', count=6)
    		time = np.fromfile(f, dtype='double', count=2)[0]
    		np.fromfile(f, dtype='uint8', count=256- 6*4- 6*8- 2*8)
    		totalparticle=0
    		for dd in npart:
        		totalparticle+=dd
    		np.fromfile(f, dtype='uint32',count=1)

    		np.fromfile(f, dtype='uint32',count=1)
    		pos = np.fromfile(f,dtype='float32',count=totalparticle*3)
    		np.fromfile(f, dtype='uint32',count=1)
	
    		np.fromfile(f, dtype='uint32',count=1)
    		vel = np.fromfile(f,dtype='float32',count=totalparticle*3)
	
		pos=np.reshape(pos,[totalparticle,3])
		vel=np.reshape(vel,[totalparticle,3])

		if a=="position":
			plt.scatter(pos[40000:,1],pos[40000:,0])
			plt.savefig("graph_%s_position.png" %(filename))

		if a=="mass":
			print mass
			#plt.scatter(mass)
			#plt.savefig("graph_%s_position.png" %(filename))
			histogram = plt.hist(mass,80)
			plt.title('Histogram mass')
			plt.xlabel('mass')
			plt.ylabel('counts')
			plt.savefig("histo_%s.png" %(filename))
			plt.close()

		if a=="velocity":
			plt.scatter(vel[40000:,1],vel[40000:,0])
			plt.savefig("graph_%s_velocity.png" %(filename))
			
		else:
			print "HELLO"

if __name__ == "__main__":
	import sys
	readsnap(str(sys.argv[1]),str(sys.argv[2]))
