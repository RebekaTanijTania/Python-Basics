
###numpy Example
import numpy as np

l = [11.5,33.0,55.5,77.5,99.0]

print(l.index(l[4]))
print(l[4])

ar = np.array(l)
print(type(ar))
print(np.ndim(ar))
print(np.size(ar))

print(ar.dtype)
print(ar)
print(ar.astype("i"))
#%%
a = ((1,2),(3,4))
array_new = np.array(a)
print(array_new.dtype)
z = array_new.reshape(2,2)
print(z)
#%%
##spli matrixB  
m1 = np.arange(0,12,1).reshape(2,2,3)
print(m1)
#%%
#### dsplit
import numpy as np
array1 = np.arange(0,12).reshape(2,2,3)
print(np.dsplit(array1,3))

#%%
## random number generator
import numpy as np
p1 = np.array([1,2,3])
p2 = np.array([4,5,6])
print(p1.dtype)
p3 = np.concatenate((p1,p2))
print(p3)

q1 = np.array(([1,2],[3,4]))
q2 = np.array(([5,6],[7,8]))

q3 = np.concatenate((q1,q2), axis = 0)
print(q3)
# %%
##using hstack and vsack
h1 = np.array([1,2,3])
h2 = np.array([4,5,6])
h3 = np.hstack((h1,h2))
print(h3)

v1 = np.array([1,2,3])
v2 = np.array([4,5,6])
v3 = np.vstack((v1,v2))
print(v3)

d1 = np.array([1,2,3])
d2 = np.array([4,5,6])
d3 = np.dstack((d1,d2))
print(d3)
#%%
import random
r = random.randrange(0,10)
print(r)

r1 = []
for i in range(10):
    j = random.randint(0,30)
    r1.append(j)
print(r1)
#%%
import numpy as np
import array as arr
a1 = arr.array("i",([1,2,3]))
a2 = arr.array("i",([4,5,6]))
a3 = a1+a2
print(a3.append(100))
a = [x for x in a3 if x%2==0]
print(a)
# %%
