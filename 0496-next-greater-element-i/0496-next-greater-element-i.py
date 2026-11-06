class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        ans = [-1]*len(nums1)
        for i in range(len(nums1)):
            tar = nums2.index(nums1[i])
            for k in range(tar+1,len(nums2)):
                if nums2[k] > nums1[i]:
                    ans[i] = nums2[k]
                    break
        return ans
