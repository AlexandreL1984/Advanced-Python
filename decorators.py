#My code and notes.
#4 March 2021 Advanced Python Seminar on Decorators

def greet():
    print("Hi")

g = greet

g()

h = lambda x: x**2

h(2)

my_list = []

type(my_list)

my_list.append(5)

def hello():
    print("Hello")

def invoker(some_func):
    return some_func()

invoker(hello)

#This code brings an error
invoker(hello())

def outer(some_func):

    def inner():
        some_func()
    return inner

g = outer(hello)

g

g()

#This doesn't exist in the global scope, so it returns an error
inner()

h = 5

h
