
# List1=[1,2,3,4,5,6,7,8,9,10]
# for value in List1:
#     value=value*2
#     if value> 15:
#         break           # break will stop the loop once its condition is met, if not it will be ignored.
#     print(value)


NumberOfCandies=int(input("How many candies do you want?"))
AvailableCandies=5
i=1
while i<=NumberOfCandies:
    if i>AvailableCandies:
        print("You can have these candies but now we are out of stock")
        break                               # break function here tell to stop the while loop as if condition is no
    print("candy")                          # longer satisfied
    i=i+1
print("Thank you for shopping here")

