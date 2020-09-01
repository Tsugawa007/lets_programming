H,W,K = map(int,input().split())
nums = list( list(input()) for i in range(H))
ans = 0
for i in range(2**H):
  for j in range(2**W):
    c = 0
    for x in range(H):
      for y in range(W):
        if(i>>x & 1) == 0 and (j >> y & 1) == 0:
          if nums[x][y] == "#":
            c += 1
    if c == K:
      ans += 1
print(ans) 
