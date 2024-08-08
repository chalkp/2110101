import math

# format: x,mtsa,rep
x, mtsa, rep = str(input()).split(',')

all_digits = int('0'+x+mtsa+rep)
non_repeating = int('0'+x+mtsa)
repeating = int('0'+rep)

frac = all_digits - non_repeating # xmtsa * 99999 + rep
devi = (10 ** len(mtsa+rep)) - (10 ** len(mtsa))

gcd = math.gcd(frac, devi)

print(frac//gcd, '/', devi//gcd)
