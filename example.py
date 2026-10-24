#%%
import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt 
d3 = pd.DataFrame( {"a":['one','two','thr','four'],'b': [4,5,1,2], 'c': [8,7,6,9],'d':[6,1,3,4]})

d4 = pd.DataFrame( {"a":['two','thr','four','five'],'b': [7,0,1,2], 'c': [10,70,60,90],'d': [60,10,30,40]} )


d5 = pd.merge(d3, d4, on='a')
print(d5)
df = pd.read_csv(r"C:\Users\ahsan\Desktop\Python_DataAnalysis\Python Materials (Done)\Datasets\d.csv", delimiter = ",")

# basic thumb rule of general idea of datset
print(df.head(5))
print(df.tail(5))

# columns, dtypes, info, values
e1 = df.info()
#print(e1)

# column names
e2 = df.columns
#print(e2)

# shape and size of dataset
e3 = df.shape
#print(e3)
e4 = df.size
#print(e4)

# finding missing data (True / false), either full df or one or more columns
#e5 = pd.isna(df) or
e5 = pd.isna(df['cut'])
#print(e5)

#%%
# random location from rows
e6 = df[ 100: 120 ]
#print(e6)
# extract sungle column
e7 = df["cut"][110:121]
#print(e7)
# extract multiple columns
e8 = df[["cut", "color", 'depth']][110:121]
#print(e8)
#%%
# frequency distribution of columns in case of categorical values
e9 = df["cut"].value_counts()
#print(e9)

e10 = df["color"].value_counts()
#print(e10)
# frequency plotting

#print(e9.plot(kind="bar"))
#print(e10.plot(kind="bar"))

#%%
# fatorize and unique
e11 = pd.unique(df['cut'])
print(e11)

e12 = pd.factorize(df['cut'])
print(e12)

# rearranging data based on single column / data sorting
e13 = df.sort_values(["table"])
#print(e13)

e14 = df.sort_values(["color"])
e14["color"].head()
e15 = e14["color"].to_list()
print(e15[:50])

