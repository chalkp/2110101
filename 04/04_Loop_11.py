x = str(input())
last = x[0]
count:int = 0

output:list = []

for c in x:
  if c == last:
    count += 1
  else:
    output.append(last)
    output.append(' ')
    output.append(str(count))
    output.append(' ')
    count = 1
    last = c

output.append(last)
output.append(' ')
output.append(str(count))
output.append(' ')

print("".join(output))
