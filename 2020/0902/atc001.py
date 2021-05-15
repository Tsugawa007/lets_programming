import queue
H,W = map(int,input().split())
nums = list( list(input()) for i in range(H))
ans = "No"
for i in range(H):
  for j in range(W):
    if nums[i][j] == "s":
      x = i
      y = j
f = queue.LifoQueue()
f.put([x,y])
while f.empty() == False:
  i,j = f.get()
  if  0 <= i < H and 0 <= j < W:
    if nums[i][j] == 'g':
      ans = "Yes"
      break
    nums[i][j] = "#"
    for x, y in ([0,1], [0,-1], [1,0], [-1,0]):
      if 0 <= x + i < H and 0 <= y + j < W and nums[x+i][y+j] != "#":
        f.put([x+i,y+j])
print(ans)
