N,M,K = map(int,input().split())
usabi_map = list(False for i in range(N))
num_list = list()
for i in range(M):
    tmp = int(input())
    num_list.append(tmp-1)
    usabi_map[tmp-1] = True
    
def jump_usabi(): 
    for j in range(len(num_list)):
        usabi_map[num_list[j]] = False
        if False in usabi_map[num_list[j]+1:]:
            index = usabi_map[num_list[j]+1:].index(False) + num_list[j]+1
            usabi_map[ index ] = True
            num_list[j] = index
        else:
            num_list[j] = usabi_map.index(False)
            usabi_map[ usabi_map.index(False) ] = True

            

for i in range(K):
    jump_usabi()
    
for i in num_list:
    print(i+1)
