class Solution:
    def subarraymin(self,nums):
        st = []
        min_sumi = 0
        for i in range(len(nums)+1):
            while st and (i  == len(nums) or nums[st[-1]]>nums[i]):
                idx = st.pop()
                left = idx-st[-1] if st else idx+1
                right = i-idx
                min_sumi += (nums[idx]*left*right)
            st.append(i)
        return min_sumi
    def subarraymax(self,nums):
        st = []
        max_sumi = 0
        for i in range(len(nums)+1):
            while st and (i == len(nums) or nums[st[-1]]<nums[i]):
                idx = st.pop()
                left = idx-st[-1] if st else idx+1
                right = i-idx
                max_sumi += (nums[idx]*left*right)
            st.append(i)
        return max_sumi
    def subArrayRanges(self, nums: list[int]) -> int:
        return self.subarraymax(nums)-self.subarraymin(nums)


        