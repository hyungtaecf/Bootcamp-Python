#Strings
"hello"
'hello'
"I'm a string"

mystring = 'abcdefg'
print(mystring[0]) #a
print(mystring[-1]) #g

#Slicing
print(mystring[:]) #abcdefg
print(mystring[2:]) #cdefg
print(mystring[:3]) #abc
print(mystring[::2])#aceg

#Basic Methods
x = mystring.upper()
print(x)

mystring = "Hello World"
x = mystring.split()
print(x)

mystring = "Hello World"
x = mystring.split('o')
print(x)

    #you can't redefine a string like mystring[2]='X'

#Print Formatting
print("Item One: {x} Item Two: {y}".format(x="dog",y="cat"))
