# Lists
mylist = [1,2,3]
print(len(mylist)) #3
mylist = ['string',1,2,3,23.2,True,'asd',[1,2,3]]
mylist = ['a', 'b', 'c', 'd', 'e']
print(mylist[2])

print(mylist)
mylist[0]= "NEW ITEM"
print(mylist)

mylist.append("NEW ITEM")
print(mylist)

newlist=["x","y","z"]
mylist.extend(newlist)
print(mylist)

item = mylist.pop()
print(mylist)
print(item)

item = mylist.pop(2)
print(item)

mylist.reverse()
print(item)

mylist=[4,9,2,51,7,932,5475,0]
mylist.sort()
print(mylist)

mylist = [1,2,['x','y','z']]
print(mylist[2][1]) #y

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix[0][0])

#LIST COMPREHENSION
first_col = [row[0] for row in matrix]
print(first_col)
