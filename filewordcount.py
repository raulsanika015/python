line=""
f = open("mydata.txt", "r")
line=f.read()
line=f.read()
print(word," repeated ",line.count(word.lower())," times in file")

f.close()

