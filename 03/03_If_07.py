x = int(input())

if x > 1e10:
  x = round(x / 1e9)
  print(str(x) + 'B')
  exit(0)

if x > 1e9:
  x = round(x / 1e9, 1)
  print(str(x) + 'B')
  exit(0)

if x > 1e8:
  x = round(x / 1000000)
  print(str(x) + 'M')
  exit(0)

if x > 1e7:
  x = round(x / 1000000)
  print(str(x) + 'M')
  exit(0)

if x > 1000000:
  x = round(x / 1000000, 1)
  print(str(x) + 'M')
  exit(0)

if x > 100000:
  x = round(x / 1000)
  print(str(x) + 'K')
  exit(0)

if x > 10000:
  x = round(x / 1000)
  print(str(x) + 'K')
  exit(0)

if x > 1000:
  x = round(x / 1000, 1)
  print(str(x) + 'K')
  exit(0)

print(x)
