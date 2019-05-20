import sympy
from sympy import *
import matplotlib.pyplot as plt
import matplotlib.patches as pat

# init_printing()

x = Symbol('x')
a = Symbol('a')
b = Symbol('b')

matrix = Matrix([
    [-x,1,0,0,1],
    [1,-x,1,0,0],
    [0,1,-x,1,0],
    [0,0,1,-x,1],
    [1,0,0,1,-x]
])

answer = solve(matrix.det(), x)
energy = [a+ans*b for ans in answer]
print('energy')
print(energy)
print('-----------------------')

c1, c2, c3, c4, c5 = symbols('c1 c2 c3 c4 c5')
coefficient = Matrix([[c1, c2, c3, c4, c5]]).T

equations = [equation for equation in matrix * coefficient]
equations.append(c1**2 + c2**2 + c3**2 + c4**2 + c5**2 -1)

print('coefficient')
for ans in answer:
    print('energy:'+str(float(ans)))
    equations_subs = [equation.subs(x, ans) for equation in equations]
    coeff = solve(equations_subs)
    print(coeff)
    X=0
    fig = plt.figure()
    ax = plt.axes()
    ax.set_xlim(0, 6)
    for rad in coeff[0].values():
        
        X += 6/5
        c_up = pat.Circle(xy = (X, rad), radius = rad, color='blue')
        ax.add_patch(c_up)
        c_down = pat.Circle(xy=(X,-rad), radius = rad, color='red')
        ax.add_patch(c_down)
    print('-------------------------')

    plt.axis('scaled')
    ax.set_aspect('equal')
    plt.show()