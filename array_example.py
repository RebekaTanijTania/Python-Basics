#%%arrayexamples

import array as arr
## or
from array import *

val = array("w", ['r','e','b','e','k','a'])
print(val)

vals = arr.array("i", [1,-2,4,7,9])
print(vals)
vals.append(15)
print(vals)

for i in range(len(vals)):
    print(vals[i])

#### another option
for v in vals:
    print(v)

#%%%
new_arr = array(vals.typecode, (a+1 for a in vals))
print(new_arr)
#%%
i=0
while i<len(new_arr):
    print(new_arr[i])
    i+=1
    #%%
ar1 = array("i",[])

n  = int(input("how many array elements?"))

for i in range(n):
    x =int(input("Enter next array value:"))
    ar1.append(x)
print(ar1)
#%%searching array elemnts
s_val = int(input("enter the search value:"))
k=0
for z in ar1:
    if z == s_val:
        print(z, "found in the array index", k)
        break

    k+=1
## Same task using index function
print(ar1.index(s_val))
#%% For Multi dimentional array
from numpy import *

mdim_array = vals + new_arr
print(mdim_array)