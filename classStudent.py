class Student:
     __Rollno=1
     def __init__(self,name,age):
          self.__name=name
          self.__age=age
          self.__rollno=Student.__Rollno
          Student.__Rollno+=1
          print("increased")

     def print_Student(self):
          print("Name:",self.__name,"\nAge:",self.__age,"\nRoll Number:",self.__rollno)
          


