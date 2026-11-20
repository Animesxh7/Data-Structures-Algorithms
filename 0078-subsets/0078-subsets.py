from itertools import combinations
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []
        for i in range(len(nums)+1):
            res += [list(k) for k in combinations(nums,i)]
        return res