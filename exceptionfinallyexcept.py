
try:
   i=int(input("Nuber pls:"))
  
   fh=open("testfile2", "r")
   fh.write("This is my test file for exception handling!!")
except IOError:
    print ("Error: can\'t find file or read data")
except Exception:
    print ("Error: math error")
finally:
      print ("Going to close the file")
      #fh.close()

