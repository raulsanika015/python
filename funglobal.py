
def printer():
     global x
     x=100
     print("in function",x)
     return
x=10
printer()
print("outside ",x)
