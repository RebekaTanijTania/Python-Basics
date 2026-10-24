def info(a, *b):
    a=8
    print(id(a))
    print(b)
    sum = globals()['a']
    for d in b:
        sum+= d
    print("Result=",sum)

a = 10
print(id(a))
info(a, 2,3,4,5)

def info2(a, **kword):
    print(a)
    print(kword)
    for i,j in kword.items():
        print(i,j)

info2(20, name="RTT", Age=44, City="Dhaka")

def count(l):
    Even = 0
    Odd = 0
    for i in l:
        if i%2 == 0:
            Even += 1
        else:
            Odd += 1
    return Even, Odd


lst = [1,22,3,44,5,7,88,9]

E, O = count(lst)

print("Even={} and Odd= {}".format(E,O))

def fibo(n):
    a = 0
    b = 1
    print(a, end=" ")
    print(b, end=" ")
    prev = b
    cur = a + b
    print(cur, end=" ")
    for i in range(2,n+1):
        temp = prev
        n_cur = temp + cur
        prev = cur
        cur = n_cur
        print(n_cur, end=" ")


fibo(int(input("Enter Length of Fibbonacci series:")))