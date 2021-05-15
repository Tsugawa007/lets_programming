N = int(input())
ans = 0
for a in range(1, N):
  print((N - 1) // a)
  # (N - 1) // c は、bとcの通りの数
  ans += (N - 1) // a
print(ans)
