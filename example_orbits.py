import sys
import math
from runge import *

# Calculating the orbits of sun-earth system
# NOTE: without correction of other celestial bodies

# dx_i/dt = v_i ; dv_i /dt = -alpha* x_i/r^3
# where alpha = G M_{sun}
def Force(i, t, xv):
    alpha = 1.32754125e20;
    r = math.sqrt(xv[0]*xv[0]+xv[1]*xv[1])
    if i==0:
        return xv[2] 
    elif i==1:
        return xv[3]
    elif i==2:
        return -(alpha*xv[0])/(r*r*r)
    elif i==3:
        return -(alpha*xv[1])/(r*r*r)
    else:
        print "something is wrong \n"
        return 0

# some parameters for initial conditions:
AU = 1.496e11
V = 30000.0 # initial velocity
result = [0] *4
y0 = [0.0,AU,-V,0.0]

T = 7.0e4 # a random time


err = 1e-5 # relative error

runge_drive(4,0.0,T,y0,Force,err,result)
print result # print the results for t = T


#Plotting (if you don't have pyplot then remove the lines below)
import matplotlib.pyplot as plt

x=[]
y=[]
Npts = 100 #number of points for the graph
T0 = 0.0
Tf = 1.1*3.154e7 # a bit over a year in seconds
h = (Tf-T0)/Npts
# placing the x-y values in a list
# TODO: have runge_drive give intermediate values
for k in range(0,Npts):
    T = T0 + k*h
    runge_drive(4,T-h,T,y0,Force,err,y0)
    x +=[y0[0]]
    y +=[y0[1]]

plt.plot(x,y)
plt.title('Orbital Trajectory')
plt.xlabel('x in meters')
plt.ylabel('y in meters')
plt.show()
