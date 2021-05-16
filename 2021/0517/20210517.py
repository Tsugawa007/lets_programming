nums1 = [1,2] 
nums2 = [-2,-1]
nums3 = [-1,2]
nums4 = [0,2]
class Solution:
    def fourSumCount(self, nums1: list, nums2: list, nums3: list, nums4: list) -> int:
        d = dict()
        for a in  nums1:
            for b in nums2:
                temp = a + b
                if temp not in d:
                    d[temp]=1
                else:
                    d[temp]+=1
        ans = 0
        for n1 in nums3:
            for n2 in nums4:
                tmp = 0  - (n1 + n2)
                if tmp in d: 
                    ans += d[tmp]
        return ans
ans = Solution().fourSumCount(nums1,nums2,nums3,nums4)
print(ans)
