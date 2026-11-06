class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        ans = []
        nge = {}
        st = []
        for j in range(len(nums2)-1,-1,-1):
            while st and st[-1]<=nums2[j]:
                st.pop()
            if st:
                nge[nums2[j]] = st[-1]
            else:
                nge[nums2[j]] = -1
            st.append(nums2[j])
        for i in nums1:
            ans.append(nge[i])
        return ans