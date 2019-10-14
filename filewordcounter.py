line=""
word=""
f = open("mydata.txt", "r")
line=f.read()
word=input("Enter word to search:")
print(word,"came in file for",line.count(word),"times")
f.close()

