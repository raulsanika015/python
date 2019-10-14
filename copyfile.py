f=open("d:\\one.txt","r")
f2=open("d:\\two.txt","w")
while(True):
     data=f.readline()
     if data=="":
          print("File over")
          break
     f2.write(data)
f.close()
f2.close()
