import math 

def funcion(x,y):
	return (2*y - 2*x**2 +x -3)

def k1(h,t,y):
	return h*(funcion(t,y))
def k2(h,t,y):
	return h*(funcion(t+0.5*h,y +0.5*k1(h,t,y)))
def k3(h,t,y):
	return h*(funcion(t+0.5*h,y +0.5*k2(h,t,y)))
def k4(h,t,y):
	return h*(funcion(t+h,y+k3(h,t,y)))

y1= 1.0+(1.0/6.0)*(k1(0.1,0,1.2) + 2.0*k2(0.1,0.0,1.2)+ 2.0*k3(0.1,0.0,1.2)+k4(0.1,0.0,1.2))
y2= y1 +(1.0/6.0)*(k1(0.1,0.0,y1) + 2.0*k2(0.1,0.0,y1)+ 2.0*k3(0.1,0.0,y1)+k4(0.1,0.0,y1))

print (y1)
print (y2)
  	
