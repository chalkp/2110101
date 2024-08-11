h = int(input())
triange:list = []

for i in range(h):
  if i == h-1:
    for j in range(i*2+1):
      triange.append('*')
    break

  for j in range(h-i-1):
    triange.append('.')
  triange.append('*')
  
  if i:
    for j in range(i*2-1):
      triange.append('.')
    triange.append('*')
  triange.append('\n')

print("".join(triange))
