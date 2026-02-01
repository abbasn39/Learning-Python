print("\nRemove comment from one of the programs to execute it")

#print("\nProgram 1\n")
# print("This Program will check if the number you enter is less than or greater than 55")
# X=2
# Y=55
#
# Z=int(input("Please enter the number you want to check\n\n"))
#
# if Z>Y:
#     print("The number is greater than 55")
# elif Z==Y:
#     print("The number is equal to 55")
# else:
#     print("The number is less than 55")
#

#print("\nProgram 2\n")
# List_A= [1,2,3,4,5,6,7,8,9,10]
#
# if int(input("Please enter the number you want to check\n\n")) in List_A:
#     print("Yes this Number is in the list")
#
# else:
#     print("No this Number is not in the list")
#
#
##print("\nProgram 3\n")
#
# Age=float(input("Please enter your age\n\n"))
# if 7<=Age<=100:
#     if Age>18:
#         print("Yes, you are allowed to drive if you have a license")
#     elif Age==18:
#         print("Please contact us as we have to physically verify your age")
#     else:
#         print("No,you can not drive because you are under 18")
# else:
#     print("Please only enter a number between 7 and 100")
#

                    # if condition1:
                    #     # code runs if condition1 is True
                    # elif condition2:
                    #     # code runs if condition1 is False and condition2 is True
                    # else:
                    #     # code runs if all above conditions are False

                    # CONDITIONS
                    # ==    (Equal to)
                    # !=    (Not Equal to)
                    # >     (Greater than)
                    # <     (Less than)
                    # >=    (Greater than or equal to)
                    # <=    (Less than or Equal to)

                    # You can also use 'and' between the above conditions like 18>=Age and Age<=30, Range from 18-30


# SHORTHAND IF ELSE STATEMENTS
XX=int(input("Enter Number 1\n"))
YY=int(input("Enter Number 2\n"))
print("Number 1 is greater than Number 2") if XX>YY else print("Number 2 is greater than Number 1")