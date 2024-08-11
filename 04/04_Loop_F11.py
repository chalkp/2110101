def RLE(t):
  # if t is an empty string
  if len(t) == 0:
    return list([])
  
  last = t[0]
  count:int = 0

  output:list = []

  for c in t:
    if c == last:
      count += 1
    else:
      output.append([last, count])
      count = 1
      last = c

  output.append([last, count])

  return output

exec(input())
