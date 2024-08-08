sales = str(input()).split(' ')
sum = int(0)

for i in sales:
  if (i != ''):
    sum += int(i)

print(sum)
