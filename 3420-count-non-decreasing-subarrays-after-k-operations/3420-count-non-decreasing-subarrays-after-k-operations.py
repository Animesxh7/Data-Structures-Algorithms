from collections import deque
class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        # count = 0
        # for i in range(len(nums)):
        #     res = []
        #     diff = 0
        #     for j in range(i,len(nums)):
        #         if res and nums[j]<res[-1]:
        #             diff+=(res[-1]-nums[j])
        #             res.append(res[-1])
        #         else:
        #             res.append(nums[j])
        #         if diff <= k:
        #             count+=1
        #         else:
        #             break
        # return count
        dq = deque()
        n = len(nums)
        j = n-1
        cost = 0
        count = 0
        for i in range(n-1,-1,-1):
            while dq and nums[dq[-1]]<nums[i]:
                left = dq.pop()
                if dq:
                    right = dq[-1]
                else:
                    right = j+1
                cost+=(right-left)*(nums[i]-nums[left])
            dq.append(i)
            while cost>k:
                cost-=(nums[dq[0]]-nums[j])
                if dq[0] == j:
                    dq.popleft()
                j-=1
            count += j-i+1
        return count



