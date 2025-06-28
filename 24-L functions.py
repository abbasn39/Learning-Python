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


a=[[1, 9, 30], [5, 3, 15],[2, 8, 10],[7, 6, 25],[4, 2, 20]]
a.sort(key=lambda x:x[0])           # def x(a):
print(a)                            #     return a[0]

a.sort(key=lambda y:y[1])           # def y(a):
print(a)                            #     return a[1]

a.sort(key=lambda z:z[2])           # def z(a):
print(a)                            #     return a[2]


print("Map() function with Lambda function")
nums = [1, 2, 3, 4]
squares = list(map(lambda x: x**2, nums))
print(squares)
# lambda x: x**2                → an anonymous function that returns the square of x
# map(lambda x: x**2, nums)     → applies the lambda to each item in nums
# list(...)                     → converts the result of map into a list

#map() is a a higher order function that is used to apply a function in a iterable(like a list) and returns
# a new iterable(a map object)


                        # map(  function        ,iterable)
                        #           ^              ^
                        # map(lambda x: x**2    , nums   )

# An iterable can be anything that can be iterated over like list, tuple, string, dict,set,range, map(), filter()

print("filter() function with Lambda function")
nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)

#Filters an iterable based on a condition and returns only those items that return True.

                        # (filter(function              , iterable)
                        #             ^                      ^
                        # (filter(lambda x: x % 2 == 0  , nums)

from functools import reduce

nums = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, nums)
print(product)  # Output: 24 (1*2*3*4)