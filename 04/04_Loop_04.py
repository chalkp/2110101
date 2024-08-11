og = list(input())
copy = ['\0']*len(og)

for i in range(len(og)):
  copy[i] = og[i]
  if og[i] == '[':
    copy[i] = '('
  if og[i] == ']':
    copy[i] = ')'
  if og[i] == '(':
    copy[i] = '['
  if og[i] == ')':
    copy[i] = ']'

print("".join(copy))
