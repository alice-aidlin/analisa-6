import sympy as sp
import math
from sympy.utilities.lambdify import lambdify

def Calculate_derivative(f):
    f_prime = f.diff(x)
    return f_prime

x = sp.symbols('x')
def I(func,a,b):
    f = lambdify(x, func)
    return 0.5*(b-a)*(f(a)+f(b))

def TrapezoidalRule(func, a, b, n):
    h = float(b - a) / n
    sum=0.0
    for i in range(n):
        sum+=I(func,a,a+h)
        a+=h
    return sum

'''def TrapezError(func, a, b, h):
    f = lambdify(x, func)
    print("ƒ(x): ", func)
    xsi=((a-b)/2)
    func_tag = Calculate_derivative(func)
    ft = lambdify(x, func_tag)
    func_tagiim=Calculate_derivative(func_tag)
    ftt = lambdify(x, func_tagiim)
    print("ƒ'': ", func_tagiim)
    print("xsi: ",xsi)
    print("f''(",xsi,")= ",ftt(xsi))

    return h ** 3 / 12 * (b - a) * ftt(xsi)'''

#print(TrapezoidalRule(sp.sin(x),0,math.pi,4))


def SimpsonRule(func, a, b, n):
    f = lambdify(x, func)
    if n % 2 != 0:
        return "n must be even"
    h = (b - a) / n
    #print("Error evaluation En = ", round(SimpsonError(func(), b, a, h), 6))
    integral = f(a) + f(b)
    for i in range(1,n):
        k = a + i * h
        if i % 2 == 0:
            integral += 2 * f(k)
        else:
            integral += 4 * f(k)
    integral *= (h/3)
    return integral
#print(SimpsonRule(sp.sin(x),0,math.pi,4))

'''def SimpsonError(func, b, a, h):
    xsi = 1
    print("ƒ(x): ", func)
    f2 = sp.diff(func, x, 4)
    print("ƒ⁴: ", f2)
    diff_4 = lambdify(x, f2)
    print("ƒ⁴(", xsi, ") =", diff_4(xsi))

    return (math.pow(h, 4) / 180) * (b - a) * diff_4(xsi)'''


def RombergsMethod(f, a, b, n):
    mat = [[0 for i in range(n)] for j in range(n)]
    for k in range(n):
        mat[k][0] = TrapezoidalRule(f, a, b, 2 ** k)
        for j in range(0, k):
            mat[k][j + 1] = (4 ** (j + 1) * mat[k][j] - mat[k - 1][j]) / (4 ** (j + 1) - 1)
            print("R[{}][{}] = ".format(k, j + 1), (mat[k][j + 1]))
    return mat
print(RombergsMethod(sp.sin(x),0,math.pi,4))




