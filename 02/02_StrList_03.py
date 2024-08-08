month_english = [
  ":)",
  "January",
  "February",
  "March",
  "April",
  "May",
  "June",
  "July",
  "August",
  "September",
  "October",
  "November",
  "December"
]
normal_date = str(input())
d, m, y = normal_date.split("/")

print(month_english[int(m)], str(d)+',', y)
