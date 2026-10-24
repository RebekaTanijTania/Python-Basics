from numpy import*

arr = array([1,2,3,4.0],float)
print(arr.dtype)

for i in "Rebeka":
    if i == 'e':
        break
        print(i)
    else:
        print(i)
## find prime numbr from 2-20

for num in range(2,20):
    for i in range(2,num):
        if num%i == 0:
            #j = num/i
            #print("%d is product of %d*%d" %(num, i ,j))
            break
    else: 
        print("%d is a prime number" %num)
    
