N = int(input())
c = 0
ans = "No"
for i in range(N):
  a,b = map(int,input().split())
  if a == b:
    c += 1
  else:
    c = 0
  if c == 3:
    ans = "Yes"
print(ans)
