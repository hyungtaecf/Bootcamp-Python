# Dictionaries
my_stuff = {"key1":"value","key2":"value2"}
my_stuff = {"key1":"value","key2":"value2"}
print(my_stuff["key2"])

my_stuff = {"key1":123,"key2":"value2",'key3':{"123":[1,2,3]}}
print(my_stuff)

my_stuff = {"key1":123,"key2":"value2",'key3':{"123":["grab me",2,3]}}
print(my_stuff["key3"]["123"][0])
print(my_stuff["key3"]["123"][0].upper())

my_stuff = {'lunch':'pizza','bfast':'eggs'}
my_stuff["lunch"] = "burger"
my_stuff["dinner"] = "pasta"
print(my_stuff)
