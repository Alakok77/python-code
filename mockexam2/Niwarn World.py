"""mod doc"""
import math
def func_x(n):
    """return x"""
    x_var = 2 + (math.log(n**2, 2) / (2*n * math.log(n, 2)))
    return x_var

def func_y(n, s):
    """return y"""
    top = math.sin(math.radians(30)) + math.sqrt(2*s)
    under = func_x(n) + 3
    y_var = top / under
    return y_var

def func_z(k):
    """return z"""
    first = (func_y(k, k))**2
    top = 8456 * (func_x(k)**4)
    under = 24 * k
    z_var = first + (top / under)
    return z_var

def main():
    """print x y z"""
    n_var = float(input())
    s_var = float(input())
    k_var = float(input())
    x_var = func_x(n_var)
    y_var = func_y(n_var, s_var)
    z_var = func_z(k_var)
    print(f"X: {x_var:.1f}, Y: {y_var:.1f}, Z: {z_var:.1f}")
main()
