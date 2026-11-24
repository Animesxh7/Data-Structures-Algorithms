import math
class Solution:
    def maxLength(self, nums: List[int]) -> int:
        res = []
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                a = nums[i:j+1]
                prod = 1
                for k in range(len(a)):
                    prod*=a[k]
                b = math.gcd(*a)
                c = math.lcm(*a)
                if prod == b*c:
                    res.append(a)
        return max(map(len,res),default = 0)
                

