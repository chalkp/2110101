num = str(input())
if len(num) != 10:
  print("Not a mobile number")
elif num[0:2] in ["06", "08", "09"]:
  print("Mobile number")
else:
  print("Not a mobile number")
