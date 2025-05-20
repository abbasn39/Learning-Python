print("Section 1\n")
Dict1={"Rabia":"Sohaib","Abbas":"Cue sad music","Minahil":"Bilal"} # Notice the {} curly brackets/ Braces
                                                                   # which indicates that this is a Dictionary
    # In Dict1 'Rabia','Abbas','Minahil' are the Keys
    # In Dict1 'Sohaib','Cue sad music','Bilal' are the values
print(Dict1)

    #If you want to fetch a Value from a Key you can use the following
print(Dict1["Rabia"])               # This will print 'Sohaib'
print(Dict1["Abbas"])               # This will print 'Cue sad Music'
print(Dict1["Minahil"])             # This will print 'Bilal'


print("Section 2\n")

Siblings={"Tahir":{"Sumiyah","Waleed","Sufiyan","Khadija"},
          "Sahira":{"Ammar","Hamza","Zainab"},
       "Humaira":{"Rabia","Abbas","Minahil"},
          "Nabeela":{"Yousuf","Rameen","Arham"},
          "Uzma":{"Mahad","Aden","Jannat"},
       "Talat":{"Eman","Fatima","Bazil"},
          "Sumaira":{"Rafay","Meerub","Musa"},
          "Farwa":{"Aleezay","Anaya"}}      #

print(Siblings["Uzma"])
print(Siblings["Humaira"])


print("Section 3\n")

Dict2={"A":"1","B":"2","C":"3"}
print(Dict2)
Dict2["D"]="4"                  #Adds the key 'D' and its corresponding value '4'
print(Dict2)
Dict2["E"]="5"                  #Adds the key 'E' and its corresponding value '5'
print(Dict2)
del Dict2["A"]                  #Deletes the Key 'A' and its corresponding value which is 1
print(Dict2)
Dict2["090078601"]="telefun"
Dict2["3.142"]="Value of Pi"    #You can store strings,float,integers in the Dictionary key and values
print(Dict2)

print("\nSection 4")
    #Explanation of Copy function in Dictionaries

Dict3={"q":"11","w":"22","e":"33"}
print(Dict3)
Dict4=Dict3                 # Dict4 is pointing to Dict3 and when we delete anything from Dict4 it will delete it
                            # from Dict3 as well unless we create a shallow copy using .copy() function
del Dict4["q"]
print(Dict3)

Dict5={"First":"1","Second":"2","Third":"3"}
print(Dict5)
Dict6=Dict5.copy()
del Dict6["First"]          # Only deletes from Dict6 without affecting Dict5 as Dict6 is only a copy of Dict5.
print(Dict6)
print(Dict5)

print("\nSection 5")

    #Explanation of get function

Dict7={"Samsung":"picture quality","LG":"Long Warranty","Sony":"Best Sound"}
print(Dict7["Samsung"])     #This will print Value for Samsung only if the key 'Samsung' exists
#print(Dict7["Haier"])      #This will give an error as the key 'Haier' does not exist
print(Dict7.get("Samsung")) #Will check if key 'samsung' exists, if yes only then it will return its Value 'picture quality'
print(Dict7.get("Haier"))   #Will check if key 'Haier' exists, if yes only then it will return its Value.
                            # if the key 'Haier' does not exist it will give 'None' instead of error

    #Other functions for dictionary
Dict7.update({"TCL":"Cheap"})       #Same as ----->  Dict7["TCl"]="Cheap" but using update is better.
print(Dict7)

print(Dict7.keys())                 # Prints all keys
print(Dict7.values())               # Prints all values
print(Dict7.items())                # Prints all items pairwise in tuples. Item=(key:value)
Dict7.pop("LG")                     # Removes keys as defined in the parenthesis
print(Dict7)
Dict7.clear()                       # Clears everything from the dictionary
print(Dict7)

