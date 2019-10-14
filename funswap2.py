def swapper( a ):
   print ("before a is ",a)
   a[0]=100
   a[3]=2000
   print ("after a is ",a)
   return


a=[10,20,30,40]
print ("in code before a is ",a)
swapper(a)
print ("in code afer a is ",a)
