# OPERATORS

# 1. Arithmetic Operators	            + - * / % ** //	Math operations
# 2. Assignment Operators	            = += -= *= /=	Assigning values to variables
# 3. Comparison Operators	            == != > < >= <=	Compare values, return True/False
# 4. Logical Operators	                'and' 'or' 'not'	Combine conditions
# 5. Identity Operators	                'is' 'is not'	Check if two variables refer to same object
# 6. Membership Operators	            'in' 'not in'	Check if a value exists in a sequence
# 7. Bitwise Operators	                `&	^ ~ << >>`


print("1- Arithmatic Operators\n")
print("A=3 & B=2\n")
A=3
B=2
print((A+B),"\t\tAddition")
print((A-B),"\t\tSubtraction")
print((A*B),"\t\tMultiplication")
print((A/B),"\tFloat Division")         #Gives answer in decimal places
print((A//B),"\t\tFloor Division")      #Gives answer in whole integers(no decimal places)
print((A%B),"\t\tModulus")              #Gives the remainder after division
print((A**B),"\t\tExponent")            #A to the power B here its 3^2

# In modulus '%' most common statements are used are like if XYZ % 2== 0 which means that if XYZ is divided by 2 and the
# remainder is zero, it means that XYZ is an even number. Modulus can be used to check 'multiple of' statements.



print("\n2-Assignment Operators\n")

#        OPERATOR	            EXAMPLE	                        SAME AS
#        =	                    x = 5	                        Assigns 5 to x
#        +=	                    x += 2	                        x = x + 2
#        -=	                    x -= 2                          x = x - 2
#        *=	                    x *= 2	                        x = x * 2
#        /=	                    x /= 2	                        x = x / 2
#        //=	                x //= 2	                        x = x // 2
#        %=	                    x %= 2	                        x = x % 2
#        **=	                x **= 2	                        x = x ** 2

x=5
print(x)
x +=2
print(x)            #Automatically updates the value of x. Useful in incremental progression of code.

print("\n3-Comparison Operators")

#       Operator	    Meaning	                    Example	            Result
#       ==	            Equal to	                5 == 5	            True
#       !=	            Not equal to	            5 != 3	            True
#       >	            Greater than	            5 > 3	            True
#       <	            Less than	                5 < 3	            False
#       >=	            Greater than or equal	    5 >= 5	            True
#       <=	            Less than or equal	        5 <= 3	            False

print("See Comments\n")

print("4-Logical Operators\n")

print("And\n")
print("True and True = True")
print("False and False = False")
print("True and False = False")
print("False and True = False\n")

# Next line executes only if both conditions are met. Remove comment from example to execute program

# print("Example")
# X=int(input("Enter first Number\n"))
# Y=int(input("Enter second Number\n"))
# if X%2==0 and Y%2==0:
#     print("both are even\n")
# else:
#     print("both are not even\n")

print("or\n")
print("True or True = True")
print("True or False = True")
print("False or True = True")
print("False or False = False\n")

#Next Line executes even if one of the condition is met

# print("Example")
# C=int(input("Enter first Number\n"))
# D=int(input("Enter second Number\n"))
# if C%2==0 or D%2==0:
#     print("at least one number is even\n")
# else:
#     print("both are not even\n")

print("Not\n")
print("not True = False")
print("not False = True\n")

# Returns the opposite

# is_raining = False
#
# if not is_raining:
#     print("You can go outside!")
# else:
#     print("Take an umbrella.")

print("5-Identity Operators\n")
E=5
F=6
G=5
print(E is F)       #False---> 5 is not 6
print(E is G)       #True----> 5 is 5
print(F is not G)   #True----> 6 is not 5


print("\n6-Membership Operators\n")

ListX=[1,2,3,4,5,6,7,8,9.10]
print(1 in ListX)               #True----> 1 is present in ListX
print(44 in ListX)              #False---> 44 is not present in ListX
print(44 not in ListX)          #True---> 44 is not present in ListX


print("\n7-Bitwise Operators\n")
# Operator    | Symbol| Meaning                                 | Example (`a = 5`, `b = 3`)
# ----------- | ------| ----------------------------------------| --------------------------------------------------
# AND         | `&`   | Sets each bit to 1 **if both** are 1    | `a & b` → `0101 & 0011 = 0001` → `1`
# OR          | \`    | \`                                      | Sets each bit to 1 **if one or both** are 1
# XOR         | `^`   | Sets each bit to 1 **if only one** is 1 | `a ^ b` → `0101 ^ 0011 = 0110` → `6`
# NOT         | `~`   | Inverts all the bits (one's complement) | `~a` → `~0101 = 1010` (in 2’s complement, it's `-6`)
# Left Shift  | `<<`  | Shifts bits to the left (adds zeros)    | `a << 1` → `1010` → `10`
# Right Shift | `>>`  | Shifts bits to the right (discards bits)| `a >> 1` → `0010` → `2`


H = 5       # 0101
I = 3       # 0011

print(H & I)  # 1  (0001)
#    H(5)                       0101
#    I(3)                       0011
#    Results after AND          FFFT (0001)-----> 1

print(H | I)  # 7  (0111)
#    H(5)                       0101
#    I(3)                       0011
#    Results after OR           FTTT (0111)-----> 7

print(H ^ I)  # 6  (0110)
#    H(5)                       0101
#    I(3)                       0011
#    Results after XOR          FTTF (0110)-----> 6

print(~H)     # -6 (two's complement of 5 is -6)
#    H(5)                       0101
#    Results after NOT(~H)      TFTF (1010)-----> -6 (Look up 2's complement to understand the NOT function)

print(H << 1) # 10 (1010)
#    H(5)                               0101
#    Results after LEFT SHIFT(H<<1)     1010-----> 10 (Shifts bits to left and add zeros to the end)

print(H >> 1) # 2  (0010)
#    H(5)                               0101
#    Results after RIGHT SHIFT(H>>1)    0010-----> 2 (Shifts bits to right and discards bits at the end)

# Number after << or >> sign indicates the number of places bits will move

