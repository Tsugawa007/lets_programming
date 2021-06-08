N = int(input())
a = list(map(int,input().split()))
ans_list  = [0] * (N+1)
for i  in range(1,N+1):
    ans_list[i] = max(ans_list[i-1],ans_list[i-1]+a[i-1])
    print(ans_list)
print(max(ans_list))

#####問題#####
Nは配列の長さ
aは数値の配列
問題は、配列の中の数値を足した総和の最大数値を答えろ

##############
