import random


dice=random.randint(1,6)                     #Random integer selected in a range 1 to 6 INCLUSIVE
print(dice)

range_low= 1
range_high = 100

Number= random.randint(range_low, range_high)      # randint can take variables as arguments as well
print(Number)

x=random.random()                                  # random.random returns a random float between 0 and 1
print(x)

rps_game=["rock","paper","scissors"]
choice=random.choice(rps_game)                     # Choice allows to choose random element in a non-empty sequence
print(choice)

cards=["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
random.shuffle(cards)                              # Shuffles elements in a non-empty sequence
                                                   # Does not require a variable assigned
print(cards)

