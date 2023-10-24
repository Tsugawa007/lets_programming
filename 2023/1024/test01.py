a=0
b=0
c=0
ans_list= []
for a in range(0,10):
    for b in range(0,10):
        x = (20+a)*b
        if(x>=100):
            tmp = (x % 100) // 10
            if(tmp ==3):
                ans_list.append([x,a])
for c in range(1,10):
    for x,a in ans_list:
        y = (20+a)*c
        if y < 100:
            ans = x + y*10
            tmp_2 = (ans % 100) // 10
            if tmp_2 == 4:
                print(ans,x,y*10)
