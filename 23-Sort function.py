print("Number List Sort")
numbers=[1,4,7,2,9,6,0]
numbers.sort()
print(numbers)
# Using 'sort' sorts the list according to ascending order by default
# 'Sort' also updates the original list

print("\nNumber List Sort (Descending)")
numbers_Descending=[1,4,7,2,9,6,0]
numbers.sort(reverse=True)
print(numbers)
# Can pass arguments inside sort(Argument) for example reverse=True which sorts the list into descending order
print("\nString List Sort")
names=['Abbas','Mahad','Hamza','Arham','Rafay']
names.sort()
print(names)
# By default 'sort' function sorts strings according to alphabetical order

print("\nNumber List Sort without modifying original list")
Num=[1,4,2,7,3,9,6,0,5,8]
sorted_Num= sorted(Num)                 # Sort 'Num' and store it in sorted_Num
print(Num)                              # Prints original list
print(sorted_Num)                       # Prints sorted list
print(Num)                              # The original list remain unmodified
# If you do not want to change the original list and store the sorted list into a new variable we use 'sorted function'
# Notice the syntax is not same as 'sort' ie "Num.sort()" instead it is "Variable= sorted(Num)"

print("\nCustom key Sorting")
#When you need to sort using a custom condition you can use 'key='
print("\nlength sorting")
fruits=['apple','Mango','Tomato','kiwi','banana','pineapple','watermelon']
fruits.sort(key=len)
print(fruits)
#sorts the list according to a custom key, according to the length of the string.

print("\nString's last index alphabetical sorting")
fruits=['apple','Mango','Tomato','kiwi','banana','pineapple','watermelon','grapefruit']
fruits.sort(key=lambda fruit: fruit[-1])
print(fruits)
#sorts the list according to a custom key (alphabetical order of the string's last index in each of the list's element).

