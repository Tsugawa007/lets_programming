N = int(input())
nums_list = [int(input()) for i in range(N)]
nums_sum = N*(N+1)//2
set_sum = sum(set(nums_list))
if sum(nums_list) - set_sum == 0:
  print("Correct")
else:
  print(sum(nums_list)-set_sum,nums_sum-set_sum)
