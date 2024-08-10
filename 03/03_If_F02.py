def choose(stu1, stu2):
  id_1, gpax_1, cp_1, cal1_1, cal2_1 = stu1
  id_2, gpax_2, cp_2, cal1_2, cal2_2 = stu2
  gpax_1, gpax_2 = float(gpax_1), float(gpax_2)

  def convert_grade(letter):
    if letter == 'A':
      return 4
    if letter == 'B':
      return 3
    if letter == 'C':
      return 2
    return 0
  
  cal1_1:int = convert_grade(cal1_1)
  cal2_1:int = convert_grade(cal2_1)
  cal1_2:int = convert_grade(cal1_2)
  cal2_2:int = convert_grade(cal2_2)

  uneligible_a:bool = (cp_1 != 'A') or (cal1_1 == 0) or (cal2_1 == 0)
  uneligible_b:bool = (cp_2 != 'A') or (cal1_2 == 0) or (cal2_2 == 0)

  if uneligible_a and uneligible_b: return list([])
  if uneligible_a and (not uneligible_b): return list([id_2])
  if (not uneligible_a) and uneligible_b: return list([id_1])

  if (gpax_1 > gpax_2): return list([id_1])
  if (gpax_2 > gpax_1): return list([id_2])
  if (cal1_1 > cal1_2): return list([id_1])
  if (cal1_2 > cal1_1): return list([id_2])
  if (cal2_1 > cal2_2): return list([id_1])
  if (cal2_2 > cal2_1): return list([id_2])

  return list([id_1, id_2])

exec(input())
