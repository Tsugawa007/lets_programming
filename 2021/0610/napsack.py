#N個の品物があり、i 番目の品物のそれぞれ重さと価値が weight[i],value[i](i=0,1,...,n−1i=0,1,...,n−1)。これらの品物から重さの総和がWを超えないように選んだときの、価値の総和の最大値を求めよ。
N = int(input())
a_list = list( list(map(int,input().split()))  for i in range(N))
W = int(input())
ans_list = list( list( [0] * (W+2))  for i in range(N+2))
for i in range(N):
    for j in range(W+1):
        if j >= a_list[i][0]:
            ans_list[i+1][j] = max(ans_list[i][j-a_list[i][0]]+a_list[i][1],ans_list[i][j])
        else:
            ans_list[i+1][j] = ans_list[i][j]
print(ans_list[N][W])
