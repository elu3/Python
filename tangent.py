from math import *
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return cos(x/2)
	
def solution(a,b,eps):
    while ((f(a)*f(b)<0) and (abs(a-b)>=eps)):
        c=(a+b)/2
        if f(c)==0:
            return c
        elif (f(a)*f(c)<0):
            b=c
        elif f(b)*f(c)<0:
            a=c
    return c
  
def draw_tangent(zeroX,a,b,ile_ptk):
	separation = (b-a)/(ile_ptk-1); 
	pointX = np.arange(a, b+separation, separation)
	pointsY_f = [0]*ile_ptk 
	pointsY_tangent = [0]*ile_ptk 
	delta_x = abs(b-a)/1e6; 
	A_tangent = (f(zeroX+delta_x)-f(zeroX-delta_x)) / (2*delta_x) 
	B_tangent = -A_tangent * zeroX; 
	for p in range (0,ile_ptk): 
		pointsY_f[p] = f(pointsX[p]) 
		pointsY_tangent[p] = A_tangent * pointsX[p] + B_tangent 
	plt.plot(pointsX,pointsY_f, pointsX,pointsY_tangent) 
	plt.grid()
	plt.show()
	return 0
	
	
a = -2.0
b = 8.0
eps = 1e-4
r = solution(a,b,eps)
print (r)
print ("zero:")
draw_tangent(r,a,b,1001)
