import matplotlib.pyplot as plt
import numpy as np
import sympy as sy
from pylab import*
def factorial( n ):
    if n == 0:
        return 1
    fact = 1
    for i in range( 1, n+1 ):
        fact *= i
    return fact
 
def taylor( f, a, b, N, IV ):
    h = (b-a)/float(N)                  
    t = np.arange( a, b+h, h )
    w = np.zeros((N+1,))
    t[0], w[0] = IV
    for i in range(1,N+1):
        T = 0
        for j in range(len(f)):
            h_factor = h**(j)/float(factorial(j+1))
            T += h_factor * f[j]( t[i-1], w[i-1] )
        w[i] = w[i-1] + h * T
    return w

a, b = 0.0, 2.0
N = 10
h = (b-a)/N
IV = ( 0.0, 0.5 )
x = np.arange( a, b+h, h )
def y(x): return x/2 + x**2 - (exp(2*x)*11/20) + 7/4
f   = lambda x, y: 2*y - 2*x**2 +x -3
df  = lambda x, y: 2*y - 2*x**2 -3*x -3
ddf = lambda x, y: 2*y - 2*x**2 -3*x +3
 
w2 = taylor( [ f, df ], a, b, N, IV )
w3 = taylor( [ f, df, ddf ], a, b, N, IV )
fig, axes = plt.subplots(1, 1, figsize=(8, 6))
axes.plot( x, w2, label='2do orden' )
axes.plot( x, w3, label='3er orden' )
axes.plot( x, y(x), label='exacta' )
axes.legend(loc=4)
axes.grid(True)
plt.show()
