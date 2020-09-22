N, M = list(map(int, input().split()))
isbreak = [False] * (N+1)
for _ in range(M):
  isbreak[int(input())] = True
  dp = [0] * (N + 1)
  dp[0] = 1
  for i in range(N):
    for j in range(i+1, min(i+3, N+1)):
      if not isbreak[j]:
        dp[j] += dp[i]
        dp[j] %= 1000000007
print(dp[-1])     
