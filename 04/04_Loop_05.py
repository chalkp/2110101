word = str(input())
sentence = list(input())
processed:list = []

for x in sentence:
  if x in ['\"', '(', ')', ',', '.', '\'']:
    processed.append(' ')
    continue;
  processed.append(x)

# evil python list-string bs
processed = "".join(processed).split(' ')
count:int = 0

for x in processed:
  if x == word:
    count += 1

print(count)
