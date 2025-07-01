print("Program 1")
print("Enter your number please")
inputNUM=input()            #This will be stored as a String
print("You Entered",inputNUM) # This will print the number as a string

#int() will treat the Variable above as an integer and now operators can be used with it.
print("Multiplied by 10 the answer is:\n",int(inputNUM) * 10)
# In Program 1, line 3 takes an input which is a string by default
#In order to use it as an integer we need to convert it using int()
# In line 7 to use multiplication we cconvert inputNUM which is a string to an integer using int(inputNUM) [Typecasting]

print("Program 2")
A=input("Please enter your input\n")
B=A*5
print(B)

# In program 2 we do not type cast anything so in line 15 when A variable is multiplied by 5 it multiplies a string
# by 5 and prints the number enter 5 times.