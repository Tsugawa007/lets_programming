import itertools
N = int(input())
word = input()
s = [int(c) for c in word]
cost = list()

for i in itertools.combinations(range(N),3):
    diff = abs(  max(sum(s[i[0]:i[1]]),sum(s[i[1]:i[2]]),sum(s[i[2]:]+s[:i[0]])) - min(sum(s[i[0]:i[1]]),sum(s[i[1]:i[2]]),sum(s[i[2]:]+s[:i[0]])) )
    cost.append(diff)   
print(min(cost))
