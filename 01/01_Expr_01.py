import math

n = int(input())

blob1 = math.sqrt(math.pi*2)
blob2 = pow(n, n+(1/2)) * blob1

lb_blob3 = pow(math.e, -n + (1/(12*n + 1)))
ub_blob3 = pow(math.e, -n + (1/(12*n)))

lower_bound = blob2 * lb_blob3
upper_bound = blob2 * ub_blob3

print(lower_bound)
print(upper_bound)
