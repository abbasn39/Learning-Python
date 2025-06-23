# Iteration
print("iterative approach")
def iterative_factorial(x):
    result=1
    if x>0:
        for y in range(1,x+1):
            result=result * y
    return result
print(iterative_factorial(5))

print("recursive approach")

def recursive_factorial(x):
    if x==1 or x==0:
        return 1
    else:
        return x*recursive_factorial(x-1)

print(recursive_factorial(5))

#Recursive function steps for the above recursive factorial program
# (5*(recursive_factorial(5-1)))                    Step 1
# (5*(4*recursive_factorial(4-1)))                  Step 2
# (5*(4*(3*recursive_factorial(3-1))))              Step 3
# (5*(4*(3*(2*recursive_factorial(2-1))))           Step 4
# (5*(4*(3*(2*(1))))))                              Step 5