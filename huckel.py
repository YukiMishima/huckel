import sympy
from sympy import *

x = Symbol('x')
a = Matrix([[2,x], [4, -1]])
print(a)
answer = solve(a.det(),x)
print(answer)