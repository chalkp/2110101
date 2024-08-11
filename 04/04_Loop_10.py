def approx_u(u):
  count:int = 0
  while u:
    u //= 10
    count += 1
  return count

a = float(input())
L:float = 0
U = approx_u(a)
x = (L+U)/2

while abs(a - pow(10, x)) > 1e-10*max(a, pow(10, x)):
  cur = pow(10, x)
  if cur > a:
    U = x
  else:
    L = x
  x = (L+U)/2

print(round(x, 6))
