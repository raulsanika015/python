line=""
f = open("mydata.txt", "r")
print(f.tell())#specifies current position
print(f.seek(5))#moves ahead by 5 positions and then displays it
print(f.tell())
print(f.seek(12))
print(f.tell())
print(f.seek(10))
f.close()

