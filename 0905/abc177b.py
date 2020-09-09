N = input()
S = input()
a = 0
nums = list(N[i:i+len(S)] for i in range(len(N)) if i+len(S)-1 < len(N))
nums_max  = 0
for i in nums:
  tmp = 0
  for j in range(len(S)):
    if i[j] == S[j]:
      tmp += 1
  if nums_max < tmp:
    nums_max = tmp
print(len(S)-nums_max)
