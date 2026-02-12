i = 1

while i <= 5:               #While loop will keep running until the condition given is satisfied.
    print(i)
    i += 1               # This keeps adding 1 to 'i' and storing it in 'i' each time the while loop runs.


while True:                 # Condition for infinite loop 'True'
    num=int(input("Enter your number: \n"))
    if num==25:
        break               # Can use 'break' to exit the loop early
    else:
        print("try again")
        continue            # 'continue' keeps the loop running.


