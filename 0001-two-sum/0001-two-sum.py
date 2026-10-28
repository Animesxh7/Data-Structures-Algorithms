class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        for i,num in enumerate(nums):
            d = target - num
            if d in mp:
                return [mp[d],i]
            mp[num]  = i
        