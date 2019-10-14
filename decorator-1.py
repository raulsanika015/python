def first(msg):    
		print(msg)    
first("Hello")
second = first
second("Hello")

def f():
    
    def g():
        print("Hi, it's me 'g'")
        print("Thanks for calling me")
        
    print("This is the function 'f'")
    print("I am calling 'g' now:")
    g()

    
f()

def g():
    print("Hi, it's me 'g'")
    print("Thanks for calling me")
    
def f(func):
    print("Hi, it's me 'f'")
    print("I will call 'func' now")
    func()
          
f(g)

def f(x):
    def g(y):
        return y + x + 3 
    return g

nf1 = f(1_
nf2 = f(3)

print(nf1(1))
print(nf2(1))


def our_decorator(func):
    def function_wrapper(x):
        print("Before calling " + func.__name__)
        func(x)
        print("After calling " + func.__name__)
    return function_wrapper

def foo(x):
    print("Hi, foo has been called with " + str(x))

print("We call foo before decoration:")
foo("Hi")
    
print("We now decorate foo with f:")
foo = our_decorator(foo)

print("We call foo after decoration:")
foo(42)


def our_decorator(func):
    def function_wrapper(x):
        print("hi how are you" )
        func(x)
        print("nice meeting you")
    return function_wrapper

@our_decorator
def foo(x):
    print("i m " + str(x))

foo("Hi")

