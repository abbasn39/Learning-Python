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
    if x==1:
        return 1
    else:
        return x*recursive_factorial(x-1)

print(recursive_factorial())