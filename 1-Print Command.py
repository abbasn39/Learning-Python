"""This is a comment
Please ignore this
I'm just checking something"""

#This is also a comment but written using a different way

print("Hello World","Whats going on?",end=" ",)
#If end="" is added then print statement will end with what's between "" rather than switching to default(end="\n")
print("Are you doing okay?")
print("Yes I'm fine")
print("He said \"Call me later\"")
# Use \ if you want to use syntax sensitive strings
print("What does the fox say?")
print("Ding Ding Ding Ding Ding Ding Ding")

print("Ding Ding")
# Added a few more dings because I'm checking how GitHub works

print("More dings")

print("\nSeparators and End Arguments\n")

print("Abbas","Mahad",sep=" and ")          #Sep arguments cannot take a number input
print("Abbas","Mahad")
print("Abbas","Mahad",sep="\t&\t")          #Sep arguments can also include escape functions
print("Abbas","Mahad",sep="+")              #Sep arguments are string sensitive (spaces etc need to be provided in string)
print("Abbas","Mahad",sep="")               # No space separators

a=1
b=2
c=3
print(a,b,c,sep='--->')

print("\nEnd Arguments\n")

print("Jack and", end=' the ')              #end tells the program to end the print with the end argument string
print('Bean', end='stalk')

print("\nUse of Asterisk\n")
print("with *")
List_with_Asterisk=[1,2,3,4,5,6,7,8,9,10,11,22,33]        #Writing an asterisk * before a list means that its elements will be
print(*List_with_Asterisk)                                # unpacked and passed to the function one after another
                                            # By default, it puts a space between indices
print("without *")
List_without_Asterisk=[1,2,3,4,5,6,7,8,9,10,11,22,33]        #Writing an asterisk * before a list means that its elements will be
print(List_without_Asterisk)
print("\nMulti Line Strings\n")


print("""This           
is
a
multi
line
string""")
#Triple quotes """ and ''' indicate that this is a multi line string

print("This"
      " is"
      " not"
      " a"
      " multi"
      " line"
      " string")
# When double quotes are used you move to the next line it automatically adds quotes when switching lines but
# does not turn the print in to a multi line format.