import math
N = int(input())
nums = list()
max_distance = 0
for i in range(N):
  tmp = list(map(int,input().split()))
  nums.append(tmp)
for i in range(N):
  for j in range(i+1,N):
    if max_distance < math.sqrt( ((nums[i][0] - nums[j][0])**2) + ((nums[i][1] - nums[j][1])**2) ):
      max_distance =  math.sqrt( ((nums[i][0] - nums[j][0])**2) + ((nums[i][1] - nums[j][1])**2) )
print(max_distance)
