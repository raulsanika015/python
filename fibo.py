f0=0
f1=1
n=int(input("Enter n:"))
for i in range(0,n):
     if i<=1:
          print(i)
     else:
          fn=f0+f1
          print(fn)
          f0=f1
          f1=fn
else:
     print("Over")
     
