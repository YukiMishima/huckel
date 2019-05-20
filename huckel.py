import sympy
from sympy import *

# init_printing()

x = Symbol('x')
a = Symbol('a')
b = Symbol('b')

matrix = Matrix([
    [-x,1,0,0],
    [1,-x,1,0],
    [0,1,-x,1],
    [0,0,1,-x]
])

answer = solve(matrix.det(), x)
energy = [a+X*b for X in answer]
print('energy')
print(energy)
print('-----------------------')

c1, c2, c3, c4 = symbols('c1 c2 c3 c4')
coefficient = Matrix([[c1, c2, c3, c4]]).T

print(matrix * coefficient)