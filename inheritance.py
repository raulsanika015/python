class Parent:       
   parentdata = 10
   def __init__(self):
      print ("Calling parent's init")

   def parentMethod(self):
      print ("Calling parent's method")

   def setAttr(self, data):
      Parent.parentdata = data

   def getAttr(self):
      print ("Parent attribute :", Parent.parentdata)

class Child(Parent):
   def __init__(self):
      print ("Calling child's init")

   def childMethod(self):
      print ('Calling child method')
c=Child()
c.childMethod()
print("parent's data",getattr(c,'parentdata'))
