import math

w = float(input())
h = float(input())

mosteller = math.sqrt(w*h) / 60
heycock = 0.024265 * pow(w, 0.5378) * pow(h, 0.3964)
boyd = 0.0333 * pow(w, 0.6157 - (0.0188 * math.log10(w))) * pow(h, 0.3)

print(mosteller)
print(heycock)
print(boyd)
