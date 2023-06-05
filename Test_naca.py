import numpy as np
import matplotlib.pyplot as plt

Naca="0015"
M=int(Naca[0])/100
P=int(Naca[1])/10
XX=int(Naca[2:4])/100

npts=100


# x=np.linspace(0,1,npts)

beta=np.linspace(0,np.pi,npts)
x=(1-np.cos(beta))/2



# t=np.linspace(0,np.pi,npts)
yc=np.array(x)

dy_dx=np.zeros(npts)

for ii in range(len(x)):
    if x[ii]>=0 and x[ii]<P:
        yc[ii]=M/P**2*(2*P*x[ii]-x[ii]**2)
        dy_dx[ii]=2*M/P**2*(P-x[ii])
    elif x[ii]>=P and x[ii]<=1:
        yc[ii]=M/(1-P)**2*(1-2*P+2*P*x[ii]-x[ii]**2)
        dy_dx[ii]=2*M/(1-P)**2*(P-x[ii])
        
t=np.arctan(dy_dx)

        
a0=0.2969
a1=-0.126
a2=-0.3516
a3=0.2843
a4=-0.1036
T=XX       
yt=T/0.2*(a0*x**0.5+a1*x+a2*x**2+a3*x**3+a4*x**4)     

xu=x-yt*np.sin(t)
yu=yc+yt*np.cos(t)


xl=x+yt*np.sin(t)
yl=yc-yt*np.cos(t)
   
xf=np.hstack((x,x[::-1]))
yf=np.hstack((yu,yl[::-1]))

plt.figure()   
plt.plot(x,yu,'-g')        
plt.plot(x,yl,'-r')    
plt.axis('equal')
plt.grid('on')

plt.figure()
plt.plot(xf,yf)
plt.plot(0.3994,0,'ok')
plt.axis('equal')
plt.grid('on')