print("DEFINE(DEF) FUNCTIONS ")
print("\nProgram 1\n")
def func_1(First_Number, Second_Number):
    print(f"The first number is {First_Number}")
    print(f"The second number is {Second_Number}")

func_1(1,2)
func_1(2,4)

print("\nProgram 2\n")
def Happy_Birthday(Name,age):
#The position of the variables in the function are order sensitive
    print(f"Happy Birthday to {Name}")
    print(f"You turned {age} years old today")


Happy_Birthday("Abbas",30)
Happy_Birthday("Mahad",24)

print("\nProgram 3\n")
def add_numbers(x,y):
    z=x+y
    return z

def subtract_numbers(x,y):
    z=x-y
    return z

def multiply_numbers(x,y):
    z=x*y
    return z

def divide_numbers(x,y):
    z=x/y
    return z

print(add_numbers(1,2))
print(subtract_numbers(1,2))
print(multiply_numbers(1,2))
print(divide_numbers(1,2))

print("\nProgram 4\n")

def name_combined(first,last):
    """This function combines first and last names"""     #This is called a DocString which defines function.
    first=first.capitalize()
    last=last.capitalize()
    return first + " " + last           #Returns some data to the place where the function is called

Full_Name=name_combined("abbas","naeem")        # function name_combined is called
print(Full_Name)
Full_Name=name_combined("mahad","masood")       # function name_combined is called
print(Full_Name)

print(name_combined.__doc__)                              # This calls the DocString which explains the function
