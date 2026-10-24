import numpy as np
import pandas as pd

data = pd.read_csv(r"C:\Users\ahsan\Desktop\Python_DataAnalysis\Python Materials (Done)\Datasets\day.csv", delimiter = ",")
## print(data)

a1 = np.array(data)
#print(type(a1))

a2 = a1[  :50,  : ]

#print(a2)

a2[ :5, 0] = np.array([51,52,53,54,55])
print(np.shape(a1))

print(np.size(a2))
#%%
from pandas import Series, DataFrame
salary = Series([50000,30000, 80000, 100000, 300000], index=['abc','bcd','cde','def','efg'])
print(salary)

c = salary
print(c['bcd'], c['def'])
print(c.index)
print(c.values)

print(c[c>=80000])
#%%##
###Creating DataFrame
null = np.nan
dt = pd.DataFrame({'Catagory': (["Electronics","Men's Clothing", "Women's Clothing"]), 'Sales_in_Unit': np.array([null,3,5]), 'Date':pd.Timestamp('20261210'),'# of customers':np.array([null,null,null])})

#print(dt)
#print(dt.info())
#%%%
##fixing the missing value
print(dt.dropna(axis=0))  #remove rows having any missing values
print(dt.dropna(axis=1, how = 'all')) ## remove column having all missing value
print(dt.dropna(axis=0, how = 'all')) ##remove rows having all missing values
#print(dt.dropna(thres=3))
print(dt.dropna(how ='any')) #remove rows having any missing values
#%%  merging DataFrame one column should be common
import numpy as np
import pandas as pd
left_df = pd.DataFrame({'Category':(['Electronics', 'Men"s Clothing', 'Women"s Clothing']),'Sales_unit1':np.array([2,6,8])})
right_df = pd.DataFrame({'Category':(['Electronics', 'Men"s Clothing', 'Women"s Clothing']),'Sales_unit2':np.array([5,4,6])})

m_df = pd.merge(left_df,right_df, on = 'Category', how='left')
print(m_df)

# %%
#column rename
# rename columns
m_df.rename(columns = {'Sales_unit1':'Morning', 'Sales_unit2':'Evening'}, inplace = True)
print(m_df)

