class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        count = 0
        odd = 0
        even = 1
        sumi = 0
        for i in range(len(arr)):
            sumi += arr[i]
            if sumi%2 == 0:
                count+=odd
                even+=1
            else:
                count += even
                odd+=1
        return count%(10**9+7)
            
                

            