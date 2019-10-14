line=""
f = open("my.txt", "r")
line=f.read()
print("Words:",(line.count(" ")+line.count("\n")))
print("Lines:",line.count("\n"))
f.close()

