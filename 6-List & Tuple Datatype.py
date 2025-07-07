First_List= [1, 2, 3, 4, 5, 6]      # Notice the [] square brackets which indicates that this is a list

print("\nPrint 1")
print(First_List[0])                #Indexing of list starts from '0'
print(First_List[1])
print(First_List[2])
print(First_List[3])
print(First_List[4])
print(First_List[5])
print(First_List[-3])               #Prints the third last number according to the indexing


Second_List=[10,3.14,"Abbas",True]  #Can store different datatypes in a single list

print("\nPrint 2")
print(Second_List[0])               #Fetches and prints item on the first index
print(Second_List[1])               #Fetches and prints item on the second index
print(Second_List[2])               #Fetches and prints item on the third index
print(Second_List[3])               #Fetches and prints item on the fourth index

print("\nPrint 3")
First_List[0] = 25                  #This replaces the first item on 'First_List' with 25
print(First_List)                   #So the altered list is [25,2,3,4,5,6]

First_List.append(7)
print(First_List)                   #Adds an item to the end of the list

First_List.insert(3,8)
print(First_List)                   # Inserts the value '8' at index '3'

First_List.pop()                    # Removes the value at the last index
print(First_List)


print("\nPrint 4")
Students=["Abbas","Mahad","Rafay","Hamza","Ammar"]
print(Students)                               #Prints the Students list

print("\nPrint 5")
Marks=[56,87,45,14,59]
print(Marks)
print(Marks[3])                               #Prints Marks at index 3

Marks.sort()                                  # Arranges the list into ascending order
print(Marks)                                  #This will now print the updated list as per line 40.

Marks.reverse()                               #This will reverse the order of the list.
print(Marks)                                  # This prints the updated list. "Marks" list is now [87,59,56,45,14]
                                              # The original list is updated

Marks.remove(87)                              # Removes item within brackets from the list
print(Marks)

    # Terms Definition
    #           Mutable= Can be changed
    #           Immutable= Cannot be changed

    #List are Mutable and Tuple are Immutable

print("\nPrint 6")
First_Tuple=(1,2,3,4,5,6,7)         # Notice the () round brackets which indicates that this is a Tuple
                                    #First_Tuple(1)=85  <----- This cannot be performed because Tuples are immutable
print(First_Tuple)

Second_Tuple=(58,)                  #If there is only one item then add "," to make it a tuple
print(Second_Tuple)                 #Printed as (58,)

print("\nPrint 7")
empty_List=[]                       # Make an empty list
print(empty_List)

print(First_List)

print(len(First_List))          # Number of items

print(sum(First_List))          # Sum of numeric items

print(min(First_List))          # Smallest item

print(max(First_List))          # Largest item
