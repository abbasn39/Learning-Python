a=input("enter the first number")
b=input("enter the second number")

try:                            # in the 'try' block if the code gives an error code will jump to except block
    print(int(a)+int(b))        #'try' is used so if the code gives an error the code continues and doesn't stop.

except ValueError:              #'except' block will execute only if 'try' gives an error.
    print("Value Error")        # 'ValueError' is a built-in class(type of error)
