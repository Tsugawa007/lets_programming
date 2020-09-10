edges = [[0,1,5],[0,2,4],[1,2,1],[1,3,1],[1,4,6],[2,5,2],[4,6,3],[5,4,1],[5,6,4]]
dist = [float("inf") for i in range(7)]
dist[0] = 0
flag = True
while flag:
  flag = False
  for i in edges:
    if dist[i[1]] > dist[i[0]] +i[2]:
      dist[i[1]] = dist[i[0]] + i[2]
      flag = True
print(dist[-1])
