Var1=24
Var2="Hello"
Var3="How you doin?"
Var4= 22.5
# Type function will print the type of Variable
print("\n\n")
print(type(Var1))
print(type(Var2))
print(type(Var3))
print(type(Var4))
#We can also use operators for integers and floats. Only '+' for strings
print(Var1 * Var1)

print(Var2 + Var3)
print(Var1 * Var4)
print(Var1 -Var4)
print(Var4 - Var1)

"""
These are all fucntions.
int()
float()
str()
"""
#Example
Var5="5"
Var6="25"

print(Var5 + Var6)                  #This will give 525 as output
print(int(Var5) + int(Var6))        #This will give 30 as output because string is converted to intege


print(5*"Hello\n")                  #Prints Hello 5 times on different lines
print(13* str(int(Var5) + int(Var6)) )

    # HOW TO INTERCHANGE VALUES OF VARIABLES
a=5
b=9
a,b=b,a
print(a)
print(b)