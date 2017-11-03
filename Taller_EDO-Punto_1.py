import matplotlib.pyplot as plt
import numpy as np
import sympy
from pylab import*
from scipy import integrate
def plot_direction_field(x, y_x, f_xy, x_lim=(-5, 5), y_lim=(-5, 5), ax=None):
	f_np = sympy.lambdify((x, y_x), f_xy, modules='numpy')
	x_vec = np.linspace(x_lim[0], x_lim[1], 20)
	y_vec = np.linspace(y_lim[0], y_lim[1], 20)
	if ax is None:
		_, ax = plt.subplots(figsize=(4, 4))
	dx = x_vec[1] - x_vec[0]
	dy = y_vec[1] - y_vec[0]
	for m, xx in enumerate(x_vec):
		for n, yy in enumerate(y_vec):
			Dy = f_np(xx, yy) * dx
			Dx = 0.8 * dx**2 / np.sqrt(dx**2 + Dy**2)
			Dy = 0.8 * Dy*dy / np.sqrt(dx**2 + Dy**2)
			ax.plot([xx - Dx/2, xx + Dx/2],
			[yy - Dy/2, yy + Dy/2], 'b', lw=0.5)
	ax.axis('tight')
	ax.set_title(r"$%s$" %(sympy.latex(sympy.Eq(y(x).diff(x), f_xy))),fontsize=18)
	return ax
def euler(f,x,y,h,m):
	u = []
	v = []
	for i in range(m):
		y=y+h*f(x,y)
		x=x+h
		u=u+[x]
		v=v+[y]
	return[u,v]
sympy.init_printing(use_latex='mathjax')
x = sympy.Symbol('x')
y = sympy.Function('y')
ics = {y(0): 1}
f = y(x)+x-x**2+1
edo_sol = sympy.dsolve(y(x).diff(x)-f)
C_eq = sympy.Eq(edo_sol.lhs.subs(x, 0).subs(ics), edo_sol.rhs.subs(x, 0))
sympy.solve(C_eq)
fig, axes = plt.subplots(1, 1, figsize=(8, 6))
campo_dir = plot_direction_field(x, y(x), f, ax=axes)
f_np = sympy.lambdify((y(x), x), f)
y0 = 0
xp = np.linspace(0, 1.9, 100)
yp = integrate.odeint(f_np, y0, xp)
xn = np.linspace(0, -5, 100)
yn = integrate.odeint(f_np, y0, xn)
def f(x,y): return y-x**2+x+1
[u,v]=euler(f,0,1,0.1,20)
axes.plot(u,v,'or')
def y(x): return exp(x)+x**2+x
x=arange(0,2.1,0.1)
axes.plot(x,y(x),'ob')
axes.grid(True)
axes.plot(xn, yn, 'b', lw=2)
axes.plot(xp, yp, 'r', lw=2)
plt.show()