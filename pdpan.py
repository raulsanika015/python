'''
# creating an empty panel
import pandas as pd
p = pd.Panel()
print (p)
'''
import pandas as pd

data = {'Item1' : pd.DataFrame([11,22,33,44]), 
   'Item2' : pd.DataFrame([90,80,70,60])}
p = pd.Panel(data)
print (p['Item1'])
