def adder(a,b):
     try:
          if(a<0):
                    raise Exception(a)
          elif(b<0):
                    raise Exception(b)
     except Exception as e:
          print("Negative value not allowed negative is:",e)
     else:
          print(a+b)
     return

adder(12,-23)




     
          
          
