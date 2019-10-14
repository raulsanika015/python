#import the pandas library and aliasing as pd
import pandas as pd
'''
df = pd.DataFrame()
print(df)
'''
'''
data = [10,20,30,40,50]
df2 = pd.DataFrame(data)
print (df2)
'''
'''
data = [['INDIA',10],['PAKISTAN',-10],['USA',420]]
df = pd.DataFrame(data,columns=['COUNTRY','GRADE'])
print (df)
'''
'''
data = {'Name':['AMAR', 'ANUP', 'PANDEY', 'GEETA'],'Age':[32,28,33,28]}
df = pd.DataFrame(data)
print (df)
'''
'''
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print (df)
print(df.loc['b'])
print(df.iloc[2])
df=df.drop(0)

'''
df = pd.DataFrame([[1, 2], [3, 4]], columns = ['a','b'])
df2 = pd.DataFrame([[5, 6], [7, 8]], columns = ['a','b'])

df = df.append(df2)
print (df)
df=df.drop(0)
print ("after drop:\n",df)
