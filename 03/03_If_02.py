id_a, gpax_a, cp_a, cal1_a, cal2_a = str(input()).split(' ')
id_b, gpax_b, cp_b, cal1_b, cal2_b = str(input()).split(' ')
gpax_a, gpax_b = float(gpax_a), float(gpax_b)

def convert_grade(letter):
  if letter == 'A':
    return 4
  if letter == 'B':
    return 3
  if letter == 'C':
    return 2
  return 0

cal1_a:int = convert_grade(cal1_a)
cal2_a:int = convert_grade(cal2_a)
cal1_b:int = convert_grade(cal1_b)
cal2_b:int = convert_grade(cal2_b)

uneligible_a:bool = (cp_a != 'A') or (cal1_a == 0) or (cal2_a == 0)
uneligible_b:bool = (cp_b != 'A') or (cal1_b == 0) or (cal2_b == 0)

if uneligible_a and uneligible_b:
  print("None")
  exit(0)
if uneligible_a and (not uneligible_b):
  print(id_b)
  exit(0)
if (not uneligible_a) and uneligible_b:
  print(id_a)
  exit(0)

def check_bigger(a, b):
  if (a > b):
    print(id_a)
    exit(0)
  if (b > a):
    print(id_b)
    exit(0)
  return

check_bigger(gpax_a, gpax_b)
check_bigger(cal1_a, cal1_b)
check_bigger(cal2_a, cal2_b)

print("Both")
