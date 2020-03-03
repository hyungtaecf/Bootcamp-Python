# INTRODUCTION

s = "GLOBAL VARIABLE"

def func():
    mylocal = 10
    print(locals())
    print(globals())

func()


def hello(name="Jose"):
    return "hello "+name

print(hello())

mynewgreet = hello # The funcion was signed to the variable

print(mynewgreet())


def hello(name="jose"):
    print("THE HELLO() FUNCTION HAS BEEN RUN!")

    def greet():
        return "THIS STRING IS INSIDE GREET()"

    def welcome():
        return "THIS STRING IS INSIDE WELCOME!"
    # print(greet())
    # print(welcome())
    # print("End of hello()")
    if name == "jose":
        return greet # Returning the function itself
    else:
        return welcome # Returning the function itself

x = hello()

x()


def hello():
    return "Hi Jose!"

def other(func):
    print("HELLO")
    print(func())

other(hello)

# DECORATORS

def new_decorator(func):
    def wrap_func():
        print("CODE HERE BEFORE EXECUTING FUNC")
        func()
        print("FUNC() HAS BEEN CALLED")

    return wrap_func

@new_decorator # same as -> func_needs_decorator = new_decorator(func_needs_decorator)
def func_needs_decorator():
    print("THIS FUNCTION IS IN NEED OF A DECORATOR!")


func_needs_decorator()
