
m=23                                # Global Variable
k=56                                # Global Variable
l=474                               # Global Variable
q=25                                # Global Variable
w=66                                # Global Variable
def func1(x):
    m=3                             # Local Variable
    k=12                            # Local Variable
    p=23                            # Local Variable
    print(f"{m} <---Local Scope\n"
          f"{k} <---Local Scope\n"
          f"{l} <--- Not found in Local scope so its printed from Global scope\n")

    #q=q+25                         # can;t do this, 'q' is a global variable and can't be modified without permission
    print(q)

    global w                        # This gives function permission to modify value of a global variable
    w=w+4
    print(w,"modified global variable value")

    print(f"x={x} where x is the argument in this function")

func1(2)
# print(p)                          # This will show an error if run because this is from a function's local scope                                  # and can't be printed in a global scope.
print("\n\n")


def func2():
    e=20
    def func3():
        global e
        e=25
    print("before calling func3",e)     #This will print 20
    func3()
    print("after calling func3",e)      # This will also print 20 even after calling func3 because the value of 'e'
                                        # does not go 1 step above in the nested function rather it goes outside
                                        # the nested functions into the global scope.
                                        # If 'e' had been defined outside the function then line 33: e=25 would have
                                        # updated the value of 'e'
func2()
print(e)                               # Now this will define a variable in the global scope named 'e' which equals 25