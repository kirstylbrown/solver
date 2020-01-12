import numpy as np
import timeit

# numpy used to compute roots of polynomial
# define an array of length n+1 containing the coefficents of the polynomial
# p[0]*x**n + p[1]*x**(n-1) + ... + p[n-1]*x + p[n]  
def npSolver(n, polyCoeff, output):
    rootsArray = np.roots(polyCoeff)
    if output:
        print("The roots are: ")
        for i in range(0, n):
            print("x = " + str(rootsArray[i]))
            
   
# poly = x**2 + 3*x - 2
n = 2
polyCoeff = [1, 3, -2]
print("Numpy")
npSolver(n, polyCoeff, True)
print("Iterative time: " + str(timeit.timeit(lambda: npSolver(n, polyCoeff, False), number = 1000)/1000))
