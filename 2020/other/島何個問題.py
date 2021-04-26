N, M = map(int, input().split())
map_list = [[0]* (N+2)]
for _ in range(M):
    map_list.append([0] + list(map(int, input().split())) + [0])
map_list.append(map_list[0])
def check(x, y):
    lands = [[x,y]]
    while lands:
        x, y = lands.pop()
        map_list[x][y] = 0
        if map_list[x+1][y] == 1:
            lands.append([x+1, y])
        if map_list[x][y+1] == 1:
            lands.append([x, y+1])
        if map_list[x-1][y] == 1:
            lands.append([x-1, y])
        if map_list[x][y-1] == 1:
            lands.append([x, y-1])
count = 0
for m in range(1, M+1):
    for n in range(1, N+1):
        if map_list[m][n] == 1:
            check(m, n)
            count += 1
print(count)
