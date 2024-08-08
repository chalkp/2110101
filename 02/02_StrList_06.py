def vec_to_list(vec):
  ret_list = list(['', '', ''])
  it = int(0)
  for i in vec:
    if (i in ['-', '.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']):
      ret_list[it] = ret_list[it]+i
    if (i == ','):
      it += 1
  ret_list[0], ret_list[1], ret_list[2] = float(ret_list[0]), float(ret_list[1]), float(ret_list[2])
  return ret_list

u = str(input())
v = str(input())

u = vec_to_list(u)
v = vec_to_list(v)
ans = list(u)

for i in range(3):
  ans[i] = u[i] + v[i]

print(u, '+', v, '=', ans)
