# We are going to build a simple solver for a 1D real valued function 
import timeit

# evaluate a function f(x) for a given value x
def evalFunction(x):
    # f(x) = x**2 + 3*x - 2
    f = x**2 + 3*x - 2
    return f

# bisection method used to compute a root of f(x) = 0 where function f(x)
# continuous on interval [x1,x2] 
# determine root accurate to within specified tolerance value tol given
# values x1 and x2 such that f(x1)*f(x2) < 0
def bisectionSolver(x1, x2, tol, output):
    f1 = evalFunction(x1)
    f2 = evalFunction(x2)
    if f1 == 0:
        print("A root of f(x) = 0 is: " + str(x1))
    elif f2 == 0:
        print("A root of f(x) = 0 is: " + str(x2))
    else:
        x3 = (x1 + x2)/2
        f3 = evalFunction(x3)
        iterCount = 0
        while abs(f3) >= tol:
            f1 = evalFunction(x1)
            if f1*f3 < 0:
                x2 = x3
            else:
                x1 = x3
            x3 = (x1 + x2)/2
            f3 = evalFunction(x3)
            iterCount += 1
    if output:
        print("A root of f(x) = 0 is: " + str(x3))
        print("The error in the root is: " + str(abs(x1 - x2)))
        print("The number of iterations executed is: " + str(iterCount))
        
x1 = -4
x2 = 1
tol = 1e-4
print("Bisection method")
bisectionSolver(x1, x2, tol, True)
print("Iterative time: " + str(timeit.timeit(lambda: bisectionSolver(x1, x2, tol, False), number = 1000)/1000))