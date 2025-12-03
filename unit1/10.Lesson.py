def recursion(n: int):
  if n == 1:
    return 1
  else:
    return recursion(n - 1) + n

print(recursion(10))  