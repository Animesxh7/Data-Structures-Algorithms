class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:
        st  = []
        sumi = 0
        for i in range(len(arr)+1):
            while st and (i==len(arr) or arr[st[-1]]>arr[i]):
                idx = st.pop()
                left = idx - st[-1] if st else idx+1
                right = i-idx
                sumi+=(arr[idx]*left*right)
            if i<len(arr):
                st.append(i)
        return sumi%(10**9+7)