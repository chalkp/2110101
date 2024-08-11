sum:float = 0
i = input()
count:int = 0

while i != 'q':
  sum += float(i)
  count += 1
  i = input()

if count == 0:
  print("No Data")
  exit(0)

print(round(sum/count, 2))
