print("Section 1\n")
s=set()                         # If we do not write 'set' after = then s will be an empty tuple
print(type(s))

print("\nSection 2\n")
List1=[1,2,3,4]
Set1=set(List1)                 #Stroring a list in  the set

print(Set1)
print(type(Set1))

print("\nSection 3\n")
Tuple1=("a","b","c","d")
Set2=set(Tuple1)                #This can store a tuple in it but at random indexing

print(Set2)
print(type(Set2))

print("\nSection 4\n")
Set3=set()
Set3.add(1)
Set3.add(2)
print(Set3)
Set3.add(3)
print(Set3)                     #Total values in Set3 are {1,2,3}
Set4=Set3.union({3,4,5})        #Total values in Set4 are {1,2,3,4,5} no repeat value in sets
print(Set4)

    # DIFFERENCE BETWEEN SETS AND DICTIONARY CREATION
    # x={a,b,c}               Values only in curly brackets create a set (no colons)
    # x={}                    empty curly brackets create a Dictionary
    # x= set()                Creates empty set
    # x= {"a":1,"b":2}        Key Value pairs in Curly brackets creates a Dictionary (colons present)

print("\nSection 5\n")
Set5={11,22,55}
Set6={33,44,55}
Set7=Set5.union(Set6)
Set8=Set5.intersection(Set6)    #You need to define a separate set for functions like union and intersection
print(Set7)
print(Set8)

print("\nSection 6")
print("Sets FUNCTIONS\n")
            #SETS FUNCTIONS

Set_F = {1, 2, 3}

Set_F.add(4)                            # Add one item
print(Set_F)
Set_F.update([5, 6])                    # Add multiple items
print(Set_F)
Set_F.remove(2)                         # Removes 2 (error if not present)
print(Set_F)
Set_F.discard(10)                       # Removes 10 if present, no error if not
print(Set_F)
Set_F.pop()                             # Removes a random item because sets stores values at random
print(Set_F)
Set_F.clear()                           # Empties the set
print(Set_F)

print("\nSection 7")
print("MATHEMATICAL OPERATIONS\n")

a = {1, 2, 3}
b = {3, 4, 5}
c = {6, 7, 8}

print(a.union(b))                   # {1, 2, 3, 4, 5}             Total Elements single occurrence of each
print(a.intersection(b))            # {3}                         Intersection of both
print(a.difference(b))              # {1, 2}                      a - b (Remainder of a printed)
print(b.difference(a))              # {4, 5}                      b - a (Remainder of b printed)
print(a.symmetric_difference(b))    # {1, 2, 4, 5}                (a U b) - (a ∩ b)

                            # a | b    union
                            # a & b    intersection
                            # a - b    difference
                            # a ^ b    symmetric difference
print("\nSection 8")

print("Membership tests\n")
print(2 in a)               #Prints True if 2 is in set 'a' otherwise false
print(4 in a)               #Prints True if 4 is in set 'a' otherwise false

d = {1, 2, 7}
e = {1, 2, 3, 7}


print("Subset and Superset tests")
print(d <= e)               # True (d is subset of e)
print(e >= d)               # True (e is superset of d)
print(e <= d)               # False (e is not a subset of d)
print(d.issubset(e))        # True
print(e.issuperset(d))      # True
    # Subset: If all elements of A are in B then A is subset of B
    # Superset: If all elements of B are in A then A is the superset of B

# a = {1, 2, 3}
# b = {3, 4, 5}
# c = {6, 7, 8}
print("\nDisjoint tests\n")            # Disjoint sets: Two different sets in which no two elements are same.
print(a.isdisjoint(b))      #False (3 is present in both)
print(a.isdisjoint(c))      #True (no two elements of set 'a' and 'c' are same)

