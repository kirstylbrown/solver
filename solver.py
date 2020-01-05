# We are going to build a simple solver for a 1D real valued function 
import numpy as np
import timeit

# using numpy to compute roots of polynomial
# define an array of length n+1 containing the coefficents of the polynomial
# p[0]*x**n + p[1]*x**(n-1) + ... + p[n-1]*x + p[n]  
def npSolver(n, polyCoeff, output):
    if output:
        print("The roots are: ")
        for i in range(0, n):
            print("x = " + str(np.roots(polyCoeff)[i]))
    else:
        np.roots(polyCoeff)

def solve(f):
    print('Do some stuff here');
    
    print('For example, evaluating f...');
    print(f(3));
    print(f(2));
    print(f(1));
    print(f(0));
    
    return 3.333; # Change this to a value of x where f(x) = 0
    
# poly = x**2 + 3*x - 2
n = 2
polyCoeff = [1, 3, -2]
npSolver(n, polyCoeff, True)
print("Iterative time: " + str(timeit.timeit(lambda: npSolver(n, polyCoeff, False), number = 1000)/1000))
print()
    
x = solve(lambda x : x**2 + 3*x - 2)
print('We have found x = ' + str(x));


