M = str(input())[::-1]
N = int(input())
len_m = len(M)

if (len_m < N):
  for i in range(len_m, N):
    M = M+'0'

print(M[::-1])
