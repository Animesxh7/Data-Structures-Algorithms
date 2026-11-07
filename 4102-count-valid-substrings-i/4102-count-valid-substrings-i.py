class Solution:
    def countValidSubstrings(self, s: str) -> int:
        count = (len(s)*(len(s)+1))//2
        last_bad = -1
        for i in range(len(s)):
            if i>=2 and s[i-2:i+1] == 'abc':
                last_bad = i-2
            count -= (last_bad+1)
        return count
            
