d = int(input())
m = int(input())
y = int(input())
y = y - 543

months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if (y % 400 == 0):
  months[2] = 29
if (y % 4 == 0) and (y % 100 != 0):
  months[2] = 29

i = 1

while i < m:
  d += months[i]
  i += 1

print(d)
