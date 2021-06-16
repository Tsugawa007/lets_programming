import sys

def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.
    A1_A6 = [3,5,2,3,4,3]
    A8_A13 = [4,2,2,3,6,2]
    B1_B5 = [4,3,3,2,3]

    a1_to_a7 = [i for i in range(355,870,10)]
    a1_to_a13 = [i for i in range(360,1375,10)]

    a7_to_a1 = [i for i in range(366,1380,10)]
    a7_to_a13 = 370

    a13_to_a1 = [i for i in range(352,1370,10)]
    a13_to_a7 = 1372


    b1_to_a7 = [i for i in range(360,1370,6)]
    a7_to_b1 = [i for i in range(371,1380,6)]

    for i, v in enumerate(lines):
        print("line[{0}]: {1}".format(i, v))
        R,S,DIR,HH = map(str,v.split())
        S = list(S)
        hh = list(HH)
        if hh[0] == "0":
            H = int(hh[1])
        else:
            H = int(hh[0] + hh[1])
        H = H *60
        if R == 'A':
            if len(S) == 3:
                s = int(S[1] + S[2])
            else:
                s = int(S[1])
            
            if s < 7:
                if DIR == 'U':
                    time_add_1 = sum(A1_A6[:(s-1)])
                    time_add_2 = time_add_1
                    ans_1 = [  i+time_add_1 for i in a1_to_a7 if (i+time_add_1) >= H and (i+time_add_1) < (H+60)]
                    ans_2 = [  i+time_add_2 for i in a1_to_a13 if (i+time_add_2) >= H and (i+time_add_2) < (H+60)]
                    ans_3 = ans_1 + ans_2 
                elif DIR == 'D':
                    time_add_1 = sum(A1_A6[(s-1):])
                    time_add_2 = sum(A1_A6[(s-1):]) + sum(A8_A13)
                    ans_1 = [  i+time_add_1 for i in a7_to_a1 if (i+time_add_1) >= H and (i+time_add_1) < (H+60)]
                    ans_2 = [  i+time_add_2 for i in a13_to_a1 if (i+time_add_2) >= H and (i+time_add_2) < (H+60)]
                    ans_3 = ans_1 + ans_2                    
                    
            elif s > 7:
                if DIR == 'U':
                    time_add_1 = sum(A8_A13[:(s-1)])
                    time_add_2 = sum(A8_A13[:(s-1)]) + sum(A1_A6)
                    if H+time_add_1 <= 370:
                        ans_1 = [  i+time_add_1 for i in a7_to_a13 if (i+time_add_1) >= H and (i+time_add_1) < (H+60)]
                        ans_2 = [  i+time_add_1 for i in a1_to_a13 if (i+time_add_2) >= H and (i+time_add_2) < (H+60)]
                        ans_3 = ans_1 + ans_2
                    else:
                        ans_2 = [  i+time_add_1 for i in a1_to_a13 if (i+time_add_2) >= H and (i+time_add_2) < (H+60)]
                        ans_3 = ans_2
    
                elif DIR == 'D':
                    time_add_1 = sum(A8_A13[(s-1):])
                    time_add_2 = sum(A1_A6[(s-1)]) + sum(A8_A13)
                    if (H + time_add_1) <=  1372 and (H + time_add_1+60) <  1372:
                        ans_1 = [  i+time_add_1 for i in a13_to_a7 if (i+time_add_1) >= H and (i+time_add_1) < (H+60)]
                        ans_2 = [  i+time_add_2 for i in a13_to_a1 if (i+time_add_2) >= H and (i+time_add_2) < (H+60)]
                        ans_3 = ans_1 + ans_2  
                    else:
                        ans_2 = [  i+time_add_2 for i in a13_to_a1 if (i+time_add_2) >= H and (i+time_add_2) < (H+60)]
                        ans_3 = ans_2
            else:
                if DIR == 'U':
                    if H <= 370:
                        time_add_1 = sum(A1_A6)
                        ans_1 = [  i for i in a7_to_a13 if i >= H and i < (H+60)]
                        ans_2 = [  (i+time_add_1) for i in a1_to_a13 if (i+time_add_1) >= H and (i+time_add_1) < (H+60)]
                        ans_3 = ans_1 + ans_2
                    else:
                        time_add_1 = sum(A1_A6)
                        ans_2 = [  (i+time_add_1) for i in a1_to_a13 if (i+time_add_1) >= H and (i+time_add_1) < (H+60)]
                        ans_3 = ans_2
    
                elif DIR == 'D':
                    time_add_1 = sum(A8_A13)
                    ans_1 = [ i for i in a7_to_a1 if i >= H and i < (H+60)]
                    ans_2 = [ (i+time_add_1) for i in a13_to_a7 if (i+time_add_1)  >= H and (i+time_add_1) < (H+60)]
                    ans_3 = ans_1 + ans_2 


        if R == 'B':
            if S[0] == 'A':
                if DIR == 'D':
                    ans_1 = [  i for i in a7_to_b1 if i >= H and i < (H+60)]
                    ans_3 = ans_1
                else:
                    print("No train")
            else:
                s = int(S[1])
                if DIR == 'U':
                    time_add = sum(B1_B5[:(s-1)])
                    ans_1 = [  (i+time_add) for i in b1_to_a7 if (i+time_add) >= H and (i+time_add) < (H+60)]
                    ans_3 = ans_1
                elif DIR == 'D':
                    time_add = sum(B1_B5[(s-1):])
                    ans_1 = [  (i+time_add) for i in b1_to_a7 if (i+time_add) >= H and (i+time_add) < (H+60)]
                    ans_3 = ans_1 
        if len(ans_3) == 0:
            print("No train")      
        else:
            ans_3.sort()
            ans = str(HH) + ":"
            for i in ans_3:
                tmp_m = i % 60
                if tmp_m < 10:
                    tmp_m = "0" + str(tmp_m)
                else:
                    tmp_m = str(tmp_m)
                ans += " " + tmp_m
        print(ans)  
 

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
