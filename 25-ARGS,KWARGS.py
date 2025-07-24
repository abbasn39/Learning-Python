print("simple define function")

def add(x,y):
    return x+y

print(add(2,4))

# In the above function add(), we can only pass 2 arguments at a time, more than that,and it will give an error.

# to pass multiple arguments we use args.
# '*' here is called the unpacking operator, the name args is not as important as the unpacking operator '*'
print("\n*args function")
def addition(*args):
    total=0
    for x in args:
        total = total + x
    return total

print(addition(1,2,3,4,5,6))            # when calling the function we can pass multiple arguments
                                              # that were not predefined in def addition(here)

print("\n**kwargs function")

def print_address_values(**kwargs):
    for values in kwargs.values():
        print(values)

print_address_values(house="142",block="A",street="33",town="Model Town",city="Gujranwala")

print("\n")

def print_address_keys(**kwargs):
    for keys in kwargs.keys():
        print(keys)

print_address_keys(house="142",block="A",street="33",town="Model Town",city="Gujranwala")

print("\n")

def print_address_key_value(**kwargs):
    for key,values in kwargs.items():
        print(f"{key}:\t{values}")

print_address_key_value(house="142",block="A",street="33",town="Model Town",city="Gujranwala")

print("*args and **kwargs function\n")

def name_address(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    if "street" in kwargs:
        print(f"{kwargs.get('house')} {kwargs.get('street')}")
        print(f"{kwargs.get('block')} {kwargs.get('town')}")
        print(f"{kwargs.get('city')}")
    elif "apt" in kwargs:
        print(f"{kwargs.get('apt')} {kwargs.get('street')}")
        print(f"{kwargs.get('block')} {kwargs.get('town')}")
        print(f"{kwargs.get('city')}")
    elif "building" in kwargs:
        print(f"{kwargs.get('apt')} {kwargs.get('building')}")
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('block')} {kwargs.get('town')}")
        print(f"{kwargs.get('city')}")
    elif "block" in kwargs:
        print(f"{kwargs.get('house')}")
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('block')} {kwargs.get('town')}")
        print(f"{kwargs.get('city')}")
    else:
        for value in kwargs.values():
            print(value)

name_address("Mr","Muhammad","Abbas",
             house="142",
             block="A",
             street="33",
             town="Model Town",
             city="Gujranwala")


print()
y= "The number is:\t"
w= "The letter"
def combo(r,*args,**kwargs):           #normal arguments have to be always before the args.

    for x in args:
        print(r,x)
    for i,j in kwargs.items():
        print(w,i," corresponds to ",j)

list1= [1,2,3,4,5]
list2= {"A":"1","B":"2"}
combo(y,*list1,**list2)