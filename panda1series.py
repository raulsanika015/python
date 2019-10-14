import pandas as pd

df = pd.read_csv("Book1.csv")   
print(df.dtypes)
print(df["SALARY"].size)
df2=df[df['SALARY']>50000]
print(df2)
'''ser = pd.Series(df['SALARY'])

data = ser.head(5)
print("data is\n",data)
ser = pd.Series(df['NAME']) 
data = ser.head(13)
print("data is\n",data)
ser = pd.Series(df['CONTACT']) 
data = ser.head(10)
print("data is\n",data)
'''
