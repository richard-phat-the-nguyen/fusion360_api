
def Naca_4_digits(Naca="0012",npts=100,echelle=1,centered=False):      
    import numpy as np
    import matplotlib.pyplot as plt

    M=int(Naca[0])/100
    P=int(Naca[1])/10
    XX=int(Naca[2:4])/100

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
    # plt.figure()   
    # plt.plot(x,yu,'-g')        
    # plt.plot(x,yl,'-r')    
    # plt.axis('equal')
    # plt.grid('on')
    plt.figure()
    
    if centered==False:
        xf=xf
        plt.plot(0.3994,0,'ok')
    else:
        xf=xf-0.3394
        plt.plot(0,0,'ok')
    

    plt.plot(xf,yf)
    
    plt.axis('equal')
    plt.grid('on')
    return [xf*echelle,yf*echelle]

[x,y]=Naca_4_digits("0015",100,20,False)

