def sqrt_n_times(x, n):
 for _ in range(n):
  x = (x ** 0.5)
 return x

def cube_root(y):
 ans = y
 ans = sqrt_n_times(ans, 2)
 ans *= sqrt_n_times(ans, 2)
 ans *= sqrt_n_times(ans, 4)
 ans *= sqrt_n_times(ans, 8)
 ans *= sqrt_n_times(ans, 16)
 ans *= sqrt_n_times(ans, 32)
 return ans

def main():
 q = float(input())
 print(cube_root(q))

exec(input()) # DON'T remove this line