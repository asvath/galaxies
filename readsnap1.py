import numpy as np
import matplotlib.pyplot as plt

from evtk.hl import gridToVTK

from evtk.hl import pointsToVTK
import numpy as np


# Example 1
npoints = 100
x = np.random.rand(npoints)
y = np.random.rand(npoints)
z = np.random.rand(npoints)
pressure = np.random.rand(npoints)
temp = np.random.rand(npoints)
pointsToVTK("./rnd_points", x, y, z, data = {"temp" : temp, "pressure" : pressure})

print x
print y
print z
print temp
print pressure

with open("snapshot_001","r") as f:
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


y=pos[40000:,1]
x=pos[40000:,0]
z=pos[40000:,2]

print x



a = np.arange(0, len(x)+1)
b = np.arange(0, len(y)+1)
c = np.arange(0, len(x)+1)

vx = vel[40000:,0]

vy=vel[40000:,1]

pointsToVTK("./asha_points", x, y, z, data = {"vx" : vx})

pointsToVTK("./asha_y_points", x, y, z, data = {"vy" : vy})

#pointsToVTK("./examples", a, b, c, data = {'x': x,"y": y})


'''
print (npart)
plt.scatter(pos[40000:,1],pos[40000:,0])
plt.show()
'''
