mna:int = 999999999999999999
mxa:int = -999999999999999999
mnb:int = 999999999999999999
mxb:int = -999999999999999999

i:int = 0
x = str(input())

while (x != "Zig-Zag") and (x != "Zag-Zig"):
  if i%2:
    a, b = x.split(' ')
  else:
    b, a = x.split(' ')
  a, b = int(a), int(b)
  mna:int = min(mna, a)
  mxa:int = max(mxa, a)
  mnb:int = min(mnb, b)
  mxb:int = max(mxb, b)
  x = str(input())
  i += 1

if x == "Zig-Zag":
  print(mnb, mxa)
else:
  print(mna, mxb)
