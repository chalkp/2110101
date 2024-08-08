dozen = str(input())
checksum = int(0)

for i in range(12):
  checksum += int(dozen[i]) * (13-i)

checksum = (11 - (checksum%11)) % 10

print(dozen[0], dozen[1:5], dozen[5:10], dozen[10:12], str(checksum))
