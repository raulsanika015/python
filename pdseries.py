'''
#CSV READABLE
import pandas as pd     
df = pd.read_csv("book1.csv")   
ser = pd.Series(df['NAME']) 
data = ser.head(5)
print("part1:\n",data)
data = ser.head(5)
print("part 2:\n",data)
data = ser.head(5)
print("part 3\n",data)
'''
'''
#loc
import pandas as pd     
df = pd.read_csv("book1.csv")   
ser = pd.Series(df['NAME']) 
data = ser.head(20)
print(data.loc[2:7])
'''
'''
#iloc
import pandas as pd     
df = pd.read_csv("book1.csv")   
ser = pd.Series(df['NAME'],index=['a','b','c','d','e','f']) 
data = ser.head()
print(data)
'''`

#add()
import pandas as pd 
# reading csv file from url  
data = pd.read_csv("book1.csv") 
# creating short data of 5 rows 
d = data.head()
listx =[1,2,3,4] 
# adding list data 
# creating new column 
d["Added values"]= d["Serial added"].add(listx) 
# display 
print(d)

