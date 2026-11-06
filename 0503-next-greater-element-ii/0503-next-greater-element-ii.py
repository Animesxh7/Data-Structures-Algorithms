class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        ans = [-1]*len(nums)
        st = []
        for i in range(2*len(nums),-1,-1):
            idx = i%len(nums)
            while st and st[-1]<=nums[idx]:
                st.pop()
            if st:
                ans[idx] = st[-1]
            st.append(nums[idx])
        return ans
                    