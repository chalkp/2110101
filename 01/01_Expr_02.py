a = float(input())
b = float(input())
c = float(input())

root = (b**2) - 4*a*c
x1 = -b-(root**0.5)
x2 = -b+(root**0.5)
a = a*2
print(round(x1/a, 3), round(x2/a, 3));
