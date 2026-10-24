from tkinter import E


list = [11,3,4,9,8,15,10]

l = []
k = []
n_list = [i for i in list if i%2 ==0]
print(n_list)
for i in list:
    if i%2 == 0:
        l.append(i)
    else:
        k.append(i)

print(l)
print(k)
(age, income) = "40,200000".split(",")
print(age)
print(income)

list_with_tuple = [(1,2),(3,4),(5,6)]
print(list_with_tuple[0][1])