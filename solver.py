# We are going to build a simple solver for a 1D real valued function 

def solve(f):
    print('Do some stuff here');
    
    print('For example, evaluating f...');
    print(f(3));
    print(f(2));
    print(f(1));
    print(f(0));
    
    return 3.333; # Change this to a value of x where f(x) = 0
    
x = solve(lambda x : x*x +3*x -2)
print('We have found x = ' + str(x));
