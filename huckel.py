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
energy = [a+ans*b for ans in answer]
print('energy')
print(energy)
print('-----------------------')

c1, c2, c3, c4 = symbols('c1 c2 c3 c4')
coefficient = Matrix([[c1, c2, c3, c4]]).T

equations = [equation for equation in matrix * coefficient]
equations.append(c1**2 + c2**2 + c3**2 + c4**2 -1)

print('coefficient')
for ans in answer:
    equations_subs = [equation.subs(x, ans) for equation in equations]
    coeff = solve(equations_subs)
    print(coeff)