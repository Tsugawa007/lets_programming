#N個の正の整数 a[0],a[1],…,a[n−1]a[0],a[1],…,a[n−1] と正の整数 A が与えられる。これらの整数から何個かの整数を選んで総和が A になるようにすることが可能か判定せよ。可能ならば "YES" と出力し、不可能ならば "NO" と出力せよ
N = int(input())
a_list = list(map(int,input().split()))
A = int(input())
ans_list = list(list([False] * (A+2)) for i in range(N+2))
ans_list[0][0] = True
for i in range(N):
    for j in range(A+1):
        if j >= a_list[i]:
            ans_list[i+1][j] = ans_list[i][j-a_list[i]] | ans_list[i][j]
        else:
            ans_list[i+1][j] |= ans_list[i][j]
if ans_list[N][A]:
    print("YES")
else:
    print("NO")
