#AND
(1>2) and (2<3)

#OR
(1>2) or (2<3)

#Multiple logical operators
(1 == 2) or (2 == 3) or (4 == 4)

#If
if 1>2:
    print("First Block!")
    if 20 > 3: #In python, the blocks are separated by levels (identation)
        print("Second Block")
elif 3 == 3: #short for else if
    print("elif ran")
else:
    print("last")


#for
seq = [1,2,3,4,5,6]
for jelly in seq:
    # Code here
    print(jelly)

d={"Sam":1, "Frank":2, "Dan":3}

for k in d:
    print(k, d[k])


pairs =[(1,2),(3,4),(5,6)]

for item in pairs:
    print(item)

for tup1, tup2 in pairs:
    print(tup2)
    print(tup1)


#while
i = 1

while i<5:
    print("i is: {}".format(i))
    i+=1

#Range

for item in range(10):
    print(item)


#List Comprehension
x = [1,2,3,4]

out = []
for num in x:
    out.append(num**2)
print(out)

out = [num**2 for num in x]
print(out) #same
