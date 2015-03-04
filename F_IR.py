#The F_IR calculation. Sanders & Mirabel(1996)In egs/second
import numpy as np
def F_IRfunc(f12,f25,f60,f100,mpc):

	FIR=(10**-14)*1.8*(13.48*f12+5.16*f25+2.58*f60+f100)
	m_pc=mpc*3.0856776*10**22 #metres
	FIR=FIR*4*np.pi*(m_pc**2)
	FIR=FIR*10**7
	
	print FIR
	return FIR




if __name__ == "__main__":
    import sys
    F_IRfunc(float(sys.argv[1]),float(sys.argv[2]),float(sys.argv[3]),float(sys.argv[4]),float(sys.argv[5]))
