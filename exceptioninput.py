try:
     name=input("Enter name:")
     
     age=int(input("Enter age:"))
     assert(age>0),"Negative age given"
     if age<18:
          raise Exception(str(age)+" not adult")
     phone=input("Enter Mobile number:")
     if len(phone)<10:
          raise Exception(phone+" not enough digits")
except Exception as my:
   print ("Exception raised:",my)
finally:
     print("Thanks for trying")
     
     
