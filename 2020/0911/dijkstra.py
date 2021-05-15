edges = [
  [[1,5],[2,4]],
  [[2,1],[3,1],[4,6]],
  [[5,2]],
  [[4,3]],
  [[6,3]],
  [[4,1],[6,4]],
  []
]
dist = [float("inf")] * 7
dist[0] = 0
target = [i for i in range(7)]
while len(target) > 0:
  num_min = target[0]
  for i in target:
    if dist[i] < dist[num_min]:
      num_min = i
  minnum = target.pop(target.index(num_min))
  for i in edges[minnum]:
    if dist[i[0]] > dist[minnum] + i[1]:
      dist[i[0]] = dist[minnum] + i[1]
print(dist[-1])
