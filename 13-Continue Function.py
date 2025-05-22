i=0                 #This gives 'i' a starting value
while True:         # True is used to run the while loop.
    if i+1<5:
        i=i+1       #Updates the value of 'i' to 'i+1' only if i+1 < 5
        continue    #Will skip the  rest of the lines under it and go to start of while loop again.
    print(i+1,end=" ")
    if i==20:
        break
    i=i+1