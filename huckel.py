import sympy
from sympy import *

x = Symbol('x')
a = Symbol('a')
b = Symbol('b')

matrix = Matrix([[-x,1,0,0], [1,-x,1,0],[0,1,-x,1],[0,0,1,-x]])
answer = solve(matrix.det(), x)
energy = [a+X*b for X in answer]
print(energy)