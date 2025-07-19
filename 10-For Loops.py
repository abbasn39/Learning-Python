print("Section 1\n")

List1=["X","Y","Z"]
for item in List1:              #Print once for every item in List1
    print(item)

print("\nSection 2\n")
List2= [["Abbas","born second"],["Minahil","born Third"],["Rabia","born First"]]
                #The above is lists within a list

for Kid,born in List2:
    print(Kid,"is",born)

#Refer to for loop and print line:
#Here Abbas, Rabia, Minahil is treated as 'Kid'
#Born first, Born second and born third is treated as 'born'

Tuple1=(1,2,3,4,5)
for item in Tuple1:
    print(item)

print("\nSection 3\n")                  # Lists in List example
List3= [["Mahad",2000],["Aden",2004],["Jannat",2010]]
for item in List3:
    print(item)                         #This treats the Lists in List3 as items ie Mahad and year 2000 are one item

print("\nSection 4\n")

List4=[["Mahad",2000],["Aden",2004],["Jannat",2010]]
for Person,YOB in List4:                # Names are automatically assigned to Person
    print(Person,YOB)                   # Years are automatically assigned to YOB

print("\nSection 5\n")

Dict1={"A":"1","B":"2","C":"3"}
for item,x in Dict1.items():            #Dict1.items() returns key-value pairs as tuples
    print(item,x)

"""Dict1={"A":"1","B":"2","C":"3"}      #Dict1 by itself (without .items()) iterates over the keys only: "A", "B", "C".
for item,x in Dict1.items():            #Trying to unpack a single string (like "A") into two variables (item, x) 
    print(item,x)                       #causes an error because there aren’t two values to unpack.
"""
print("\nSection 6\n")

List5=[["Abbas",80],["Rabia",90],["Mahad",33],["Ahmad",10],["John",7]]
for Name,Marks in List5:
    if Marks > 33:
        print(Name,"has passed the exam")
    elif Marks==33:
        print(Name,"has massan massan passed the exam")
    else:
        print(Name,"has failed the exam")

print("\nSection 7\n")

list1=[[1,2],[3,4],[5,6]]

for x in list1[0:3]:        # Range of list defined in [], index 0 till 2 inclusive
    for a in x:
        break
    print(a)
print("\n")
for x in list1[0:2]:        # Range of list defined in [], index 0 till 1 inclusive
    for b in x:
        break
    print(b)
print("\n")
for x in list1[0:1]:        # Range of list defined in [], only index 0
    for c in x:
        break
    print(c)