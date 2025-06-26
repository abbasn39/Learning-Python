print("\nSubtraction using define function")
def subtract(x,y):
    return x-y

print("Def subtract",subtract(4,2))

print("\nSubtraction using Lambda function")
minus= lambda x,y: x-y
print("Lambda Minus",minus(4,1))

# Both above functions do the same thing.

# | Feature      | 'def' Function |       'lambda' Function     |
# | ------------ | -------------- | ----------------------------|
# | Named        |      Yes       |  No (anonymous)             |
# | Multi-line?  |      Yes       |  Only one expression        |
# | Reusable?    |      Yes       |  But not ideal for long use |
# | Readability? | More readable  |  Less readable if overused  |

def x(a):
    return a[0]
def y(a):
    return a[1]
def z(a):
    return a[2]
a=[[1, 9, 30], [5, 3, 15],[2, 8, 10],[7, 6, 25],[4, 2, 20]]
a.sort(key=x)
print(a)
a.sort(key=y)
print(a)
a.sort(key=z)
print(a)