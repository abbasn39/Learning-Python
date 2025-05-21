
List1=[1,2,3,4,5,6,7,8,9,10]
for value in List1:
    value=value*2
    if value> 15:
        break           # break will stop the loop once its condition is met, if not it will be ignored.
    print(value)