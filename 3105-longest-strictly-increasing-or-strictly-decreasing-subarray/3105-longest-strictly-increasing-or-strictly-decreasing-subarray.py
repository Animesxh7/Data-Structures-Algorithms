class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        res = []
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                a = nums[i:j+1]
                if a == sorted(a) and len(set(a)) == len(a):
                    res.append(a)
                elif  a == sorted(a,reverse = True) and len(set(a)) == len(a):
                    res.append(a)        
        return max(len(a) for a in res)
                