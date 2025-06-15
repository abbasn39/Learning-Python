
m=23                                # Global Variable
k=56                                # Global Variable
def func1(x):
    m=3                             # Local Variable
    k=12                            # Local Variable
    print(m,k)
    print("x=",x,"is the argument in this function")


func1(2)