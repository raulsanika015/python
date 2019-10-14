'''
import pandas as pd 
# reading csv file from url  
data = pd.read_csv("book1.csv") 
# creating short data of 5 rows 
d = data.head()  
# creating list with 5 values 
list =[1000,2000,3000,4000,5000] 
  
# adding list data 
# creating new column 
d["Added values"]= d["SALARY"].add(list) 
  
# display 
print(d)
print(d["SALARY"].prod())
print(d["SALARY"].sum())
'''

# importing pandas module  
import pandas as pd 
   
# reading csv file from url  
data = pd.read_csv("Book1.csv") 
    
# dropping null value columns to avoid errors 
data.dropna(inplace = True) 
   
# storing dtype before converting 
before = data.dtypes 
   
# converting dtypes using astype 
data["SALARY"]= data["SALARY"].astype(int) 
data["CONTACT"]= data["CONTACT"].astype(str) 
   
# storing dtype after converting 
after = data.dtypes 
   
# printing to compare 
print("BEFORE CONVERSION\n", before, "\n") 
print("AFTER CONVERSION\n", after, "\n") 
