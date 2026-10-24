def func1(x):
    return x**2

def func2(f,x):
    return f(x)

print(func2(func1,6))

## Lamda function

print(func2(lambda x: x**3, 5))

def f1(x,y=3):
    return (x + y)
print(f1(2))

def f2(a=5, b=4):
    c = (a**2) + (2*a*b) + (b**2)
    print("(a+b)**2 =",c, "when a=5, and b=4")
    return (c * f1(2))
print(f2())