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
choice=random.choice(rps_game)                     # Choice allows to choose 1 random element in a non-empty sequence
print(choice)
choices=random.choices(rps_game,k=7)               # Choices chooses k number of random elements
print(choices)
sample=random.sample(rps_game,k=0)                # sample chooses k number of distinct elements (x<=no of items)
print(sample)
# Notice only use 'k' in the arguments of choices or sample, it is not a variable.

cards=["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
random.shuffle(cards)                              # Shuffles elements in a non-empty sequence
                                                   # Does not require a variable assigned
print(cards)

uniform=random.uniform(1,6)                  # returns a random float between the range defined in arguments
print(uniform)

qwerty=["q","w","e","r","t","y","u","i","o","p"]
random.seed(3)                                     #random will return the same result for a particular seed each time
random.shuffle(qwerty)
print(qwerty)
