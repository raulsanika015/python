a=10
def fun1():
     print("from fun1",a)
     return

def fun2():
     a=200#local a newly created
     print("from fun2",a)
     return

def fun3():
     global a#accessed global
     a=1#operated on gloabal a
     print("from fun3",a)
     return
print(a)#10
fun1()#10
print(a)#10
fun2()#200
print(a)#10
fun3()#1
print(a)#10 | 1
