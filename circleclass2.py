class circle:
     'this will be documented'
     def __init__(self,radius):
          self.radius=radius
     def area(self):
          print("area of circle is ",(3.14*self.radius*self.radius))

c=circle(22.2)
c.area()

print ("circle.__doc__:", circle.__doc__)
print ("circle.__name__:", circle.__name__)
print ("circle.__module__:", circle.__module__)
print ("circle.__bases__:", circle.__bases__)
print ("circle.__dict__:", circle.__dict__ )
