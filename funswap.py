

def swapper( a,b ):
   print ("before a is ",a," b is ",b)
   t=a;
   a=b;
   b=t
   print ("after a is ",a," b is ",b)
   return


a=10
b=20
print ("in code before a is ",a," b is ",b)
swapper(a,b)
print ("in code afer a is ",a," b is ",b)
