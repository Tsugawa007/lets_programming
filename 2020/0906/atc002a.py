from collections import deque
H,W = map(int,input().split())
S_y,S_x = map(int,input().split())
F_y,F_x = map(int,input().split())
map_l = [input() for i in range(H)]
a = [[0 for i in range(W)] for j in range(H)]
b = [[0 for i in range(W)] for j in range(H)]
f = deque([])
f.append((S_y-1,S_x-1))
a[S_y-1][S_x-1],b[S_y-1][S_x-1] = 1,0
while 1:
  if len(f) == 0:break
  t = f.popleft()
  for i in [(1,0),(-1,0),(0,1),(0,-1)]:
    tmp = (t[0]+i[0],t[1]+i[1])
    if tmp[0]<0 or tmp[0]>=H:continue
    if tmp[1]<0 or tmp[1]>=W:continue
    if a[tmp[0]][tmp[1]]==1:continue
    if map_l[tmp[0]][tmp[1]]=='#':continue
    a[tmp[0]][tmp[1]] = 1
    f.append(tmp)
    b[tmp[0]][tmp[1]] = b[t[0]][t[1]] + 1
print(b[F_y-1][F_x-1])
