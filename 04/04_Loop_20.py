n = int(input())

mna:int = 999999999999999999
mxa:int = -999999999999999999
mnb:int = 999999999999999999
mxb:int = -999999999999999999

for i in range(n):
  if i%2:
    a, b = str(input()).split(' ')
  else:
    b, a = str(input()).split(' ')
  a, b = int(a), int(b)
  mna:int = min(mna, a)
  mxa:int = max(mxa, a)
  mnb:int = min(mnb, b)
  mxb:int = max(mxb, b)

if str(input()) == "Zig-Zag":
  print(mnb, mxa)
else:
  print(mna, mxb)
