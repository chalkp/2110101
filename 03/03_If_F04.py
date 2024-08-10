def is_mobile_number(number):
  if len(number) != 10:
    return False
  elif number[0:2] in ["06", "08", "09"]:
    return True
  else:
    return False

exec(input())
