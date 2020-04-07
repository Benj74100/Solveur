from numpy import *
from sympy import *
from math import *
from pylab import *
from sympy import var
import string
string.ascii_lowercase
l = list(string.ascii_lowercase)
def poly(n): #Cette fonction génère un pôlynome de degré n 
    sol = 0

for i,j in range(0,n+1)(l):
    sol += j*sol**i
return sol




def resol(a,b,c,A):
#First order differential equation with or without second member
	var("k,x,k_1,C_1,C_2,L,w,B_,M,x_1,x_2")
	k = float
	L = float
	B_ = float
	M = float
	C_1 = float
	C_2 = float
	w = float


	if a == 0: 
		res = k*exp(-1*integrate(c/b,x)) + k*exp(-1*integrate(c/b,x))*integrate(A/(b*exp(-1*integrate(c/b,x))),x) #solution générale variation de la constante
		
	else:
		#Second order differential equation with or without second member
		d = b**2 -4*(a*c)
		
	deg_sol = degree(A) #degré de la solution

	if d > 0 :
		x_1 = (-1*b + -1*sqrt(d))/(2*a) and x_2 = (-1*b + sqrt(d))/(2*a)
		res = C_1*exp(x_1*x) + C_2exp(x_2*x) #solution homogène
				
		if A == k*exp(k_1*x):
			res += L*exp(k_1*x)*poly(deg_sol) 

		elif A == k*sin(w*x) or k*cos(w*x):
			res += L*sin(w*x) + B_*cos(w*x)
				
		elif A == exp(k_1*x)*(L*sin(w*x) + M*cos(w*x)):
			deg_sol = degree(A) 
			res += poly(deg_sol)*exp(k_1*x)*(L*sin(w*x) + M*cos(w*x))
		else:
			if c != 0:
				res += poly(deg_sol)
			elif c == 0 and b != 0:
				res += poly(deg_sol + 1)
			elif b == c == 0:
				res += poly(deg_sol + 2)
			else:
				print("Error")
	elif d == 0 :

		x_1 = (-1*b)/(2*a)
		res = exp(x_1*x)*(C_1*x + C_2) #Solution homogène
				
		if A == k*exp(k_1*x):
			res += L*exp(k_1*x)*poly(deg_sol)
		elif A == k*sin(w*x) or k*cos(w*x):
			res += L*sin(w*x) + B_*cos(w*x)
		elif A == exp(k_1*x)*(L*sin(w*x) + M*cos(w*x)):
			res += poly(deg_sol)*exp(k_1*x)*(L*sin(w*x) + M*cos(w*x))
		else:
			if c != 0:
				res += poly(deg_sol)
			elif c == 0 and b != 0:
				res += poly(deg_sol + 1)
			elif b == c == 0:
				res += poly(deg_sol + 2)
			else:
				print("Error")
	elif d < 0:
				   
		x_1 = -1 * b -I*sqrt(-1*d)/(2*a) and x_2 = (-1*b + I*sqrt(-1*d))/(2*a)
		res = exp(re(x_1)*x)*(C_1*cos(im(X_1*x)) + C_2*sin(im(x_2*x))) #Solution homogène
				
		if A == k*exp(k_1*x):
			res += L*exp(k_1*x)*poly(deg_sol)
		elif A == k*sin(w*x) or k*cos(w*x):
			res += L*sin(w*x) + B_*cos(w*x)
		elif A == exp(k_1*x)*(L*sin(w*x) + M*cos(w*x)):
			res += poly(deg_sol)*exp(k_1*x)*(L*sin(w*x) + M*cos(w*x))
		else:
			if c != 0:
				res += poly(deg_sol)
			elif c == 0 and b != 0:
				res += poly(deg_sol + 1)
			elif b == c == 0:
				res += poly(deg_sol + 2)
			else:
				print("Error")
										
				   
	return res

