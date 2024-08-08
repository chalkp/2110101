def check_digit(n):
  checksum = 0
  for i in range(12):
    checksum += int(n[i]) * (13-i)

  checksum = (11 - (checksum % 11)) % 10
  return checksum
  
exec(input())
