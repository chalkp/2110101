ans = str(input())
res = str(input())

if len(ans) != len(res):
  print("Incomplete answer")
  exit(0)

count:int = 0

for i in range(len(ans)):
  if ans[i] == res[i]:
    count += 1

print(count)
