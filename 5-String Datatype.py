
Str1="Abbas is a boy"
print("Print 1")
print(Str1[0])              #The letter 'A' is at [0] index position

print("Print 2")
print(Str1[0:4])            #This print 'Abba' only because when defining a range in
                            #index the last number ie '4' in not inclusive
print("Print 3")
print(Str1[0:5])            #This prints 'Abbas' because when we enter [0:5] it
                            #includes the last letter of 'Abbas' because '5' makes the
                            # 's' inclusive in the string range
print("Print 4")
print(len(Str1))            #This prints 14 but according to index length is 13.
                            #'len' counts index '0' and starts from 1.

# A b b a s   i s   a    b  o  y           #String
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13          # Respective indices for each letter and the spaces between words

print("Print 5")
print(Str1[0:14])

print("Print 6")
print(Str1[0:25])                          # This will still print the whole string ignoring the excess indices

print("Print 7")
print(Str1[0:])                           # Prints everything including string index 0

print("Print 8")
print(Str1[:5])                           # Prints everything before string index 5 excluding index 5

print("Print 9")
print(Str1[0:5:2])                        # This skips one index. prints alternate indices inclusive of index 0

print("Print 10")
print(Str1[0:14:3])                       #Prints index 0 and then every third index till index 14

print("Print 11")
print(Str1[0:14:4])                       #Prints index 0 and then every fourth index

print("Print 12")
print(Str1[:])                            #Prints everything

print("Print 13")
print(Str1[::2])                          #Prints every second index including the index 0

print("Print 14")
print(Str1[-14:len(Str1)])                #Prints the whole string but we use len(Str1) as the upper limit in the range
                                          # len(Str1) defines the whole length of the string
                                          # You can also write the value of len(Str1) in the range to get same output
    #" print(Str1[-14:len(Str1)]) " is equal to " print(Str1[0:14]) " is equal to print(Str1[-14:])

print("Print 15")
print(Str1[::-1])                         #Prints every string index starting from the end

print("Print 16")
print(Str1[::-2])                         #Prints every second string index starting from end including the first string
                                          # index from the end ie "y"

print("Print 17")
print(Str1.isupper())                   #Checks if the string is in Upper Case
print(Str1.islower())                   #Checks if the string is in Lower Case
print(Str1.isdigit())                   #Checks if the string is in Digits (Only checks for 0-9 digits)
print(Str1.isalpha())                   #Checks if the string is in alphabetical
print(Str1.isalnum())                   #Checks if the string is in AlphaNumeric
print(Str1.isspace())                   #Checks if the string is all spaces
print(Str1.isnumeric())                 #Checks if the string is in numbers(checks Unicode mathematical characters too)

print("Print 18")
print(Str1.endswith("boy"))             #True
print(Str1.startswith("Abbas"))         #True
print(Str1.startswith("boy"))           #False
print(Str1.endswith("Abbas"))           #False


print(Str1.count("a"))                  #Counts the numbers of "a" (Notice it does not count uppercase "A")

print(Str1.capitalize())                                    #Capatalizes the first index
print(Str1.lower())                                         #Turns first index to lower case
print(Str1.swapcase())                                      # Swaps upper with lower case and vice versa
print(Str1.find("boy"))                                     # Returns the index numbers where mentioned string starts
print(Str1.lower())                                         # Converts whole string to lower case
print(Str1.upper())                                         # Converts whole string to upper case
print(Str1.title())                                         # Capitalizes first character of each word

print(Str1.replace("Abbas","Naeem"))           # Replaces string print(Str1.replace("old","New"))

