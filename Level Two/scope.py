x = 25
def my_func():
    x = 50
    return x

print(x) #25
print(my_func()) #50
my_func()
print(x) #25


# Local
lambda x: x**2

# Enclosing function locals
name = "This is a global name!"

def greet():
    name = "sammy"

    def hello():
        print("hello "+name)

    hello()

greet()


def func():
    global x
    x = 1000

print("before function call, x is: ",x)
func()
print("after function call, x is: ",x)
print(x)
