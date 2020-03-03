# print("hello) # Syntax Error

mylisthere = [1,2,3]
# print(mylist) # Name Error

try:
    f = open("simple.txt","r")
    f.write("Test write to simple text!")
except: # except IOError: # Specific error
    print("ERROR: COULD NOT FIND FILE OR READ DATA!")
else:
    print("SUCCESS!")
    f.close()
finally:
    print("I ALWAYS WORK NO MATTER WHAT!")

print("continuing code")
