N,M = map(int,input().split())
map_list = [['1' for i in range(N+2)]]
for i in range(M):
    tmp_list = list(map(str,input().split()))
    for j in range(len(tmp_list)):
        if tmp_list[j] == 's':
            tmp_list[j] = '0'
            x,y= j+1,i+1
    map_list.append(['1']+tmp_list+['1'])
map_list.append(map_list[0])
pos = [[y,x,0]]
ans = None
while len(pos) > 0:
    x,y,depth = pos.pop(0)

    if map_list[x][y] == 'g':
        ans = depth
        break
    map_list[x][y] = '1'

    if map_list[x-1][y] != '1':
        pos.append([x-1,y,depth+1])
    if map_list[x+1][y] != '1':
        pos.append([x+1,y,depth+1])
    if map_list[x][y-1] != '1':
        pos.append([x,y-1,depth+1])
    if map_list[x][y+1] != '1':
        pos.append([x,y+1,depth+1])  
if ans == None:
    print("Fail")    
else:
    print(ans)
