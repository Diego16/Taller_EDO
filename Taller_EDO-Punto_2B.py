import matplotlib.pyplot as plt
import numpy as np
import sympy as sy
from pylab import*
def heun( f, a, b, N, IV ):
	h = (b-a)/float(N)
	t = np.arange( a, b+h, h )
	w = np.zeros((N+1,))
	t[0], w[0] = IV
	for i in range(1,N+1):
		f1 = f( t[i-1], w[i-1] )
		f2 = f( t[i-1] + (2.0/3.0) * h, w[i-1] + (2.0/3.0) * h * f1 )
		w[i] = w[i-1] + h * ( f1 + 3.0 * f2 ) / 4.0
	return w
a, b = 0.0, 2.0
N = 10
h = (b-a)/N
IV = ( 0.0, 0.5 )
x = np.arange( a, b+h, h )
def y(x): return x/2 + x**2 - (exp(2*x)*11/20) + 7/4
f = lambda x, y: 2*y - 2*x**2 +x -3
w2 = heun( f, a, b, N, IV )
fig, axes = plt.subplots(1, 1, figsize=(8, 6))
axes.plot( x, w2, label='Heun' )
axes.plot( x, y(x), label='exacta' )
axes.legend(loc=4)
axes.grid(True)
plt.show()