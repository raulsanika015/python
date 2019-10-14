line=""
linecount=1
f = open("mydata.txt", "r")
while True:
     line=f.readline()
     if line=="":
          break
     
     print("line",linecount,":",line)
     linecount+=1
f.close()

