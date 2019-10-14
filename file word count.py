line=""

f = open("mydata.txt", "r")
line=f.read()
print("Words in file",int(line.count(" ")+line.count("\n")))

f.close()

