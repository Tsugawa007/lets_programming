N,S = map(int,input().split())
x = -1
y = -1
z = -1
for i in range(N+1):
  for j in range(N+1):
    if N-(i+j) >= 0 and S == ( 10000*i + 5000*j + 1000*(N-(i+j)) ):
      x = i
      y = j
      z = N-(i+j)
      break
print(x,y,z)
