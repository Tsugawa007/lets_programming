from collections import deque
H,W = map(int,input().split())
s_y,s_x = map(int,input().split())
f_y,f_x = map(int,input().split())
map_list = [input() for i in range(H)]
a = [[0 for i in range(W)]for i in range(H)] 
b = [[0 for i in range(W)]for i in range(H)] #ゴールについた時の移動した回数
a[s_y-1][s_x-1],b[s_y-1][s_x-1] = 1,0
f = deque()
f.append((s_y-1,s_x-1))
while 1:
  if len(f) == 0:break
  t = f.popleft()
  for i in [(0,1),(0,-1),(1,0),(-1,0)]:
    tmp = (t[0]+i[0],t[1]+i[1])
    if tmp[0]<0 and tmp[0]>H:continue
    if tmp[1]<0 and tmp[1]>W:continue
    if a[tmp[0]][tmp[1]] == 1:continue
    if map_list[tmp[0]][tmp[1]] == "#":continue
    a[tmp[0]][tmp[1]] = 1
    f.append(tmp)
    b[tmp[0]][tmp[1]] = b[t[0]][t[1]]+1
print(b[f_y-1][f_x-1])
