import math

blob1 = math.pi;

blob2 = math.factorial(10) / math.pow(8, 8);

blob3_1 = math.log(9.7);
blob3_2 = (7 / math.sqrt(71)) - math.sin(math.radians(40));
blob3 = math.pow(blob3_1, blob3_2);

blob4 = math.pow(1.2, (2.3 ** (1./3.)))

ans = (blob1 - blob2 + blob3) / blob4

print(round(ans, 6))
