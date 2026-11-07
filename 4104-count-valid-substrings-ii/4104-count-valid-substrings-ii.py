class Solution:
    def countValidSubstrings(self, s: str) -> int:
        count = 0
        last_bad = -1
        a = -1
        b = -1
        for i in range(len(s)):
            if s[i] == 'a':
                a = i
            elif s[i] == 'b' and a!=-1:
                b = a
            elif s[i] == 'c' and b!=-1:
                last_bad = max(last_bad,b)
            count+=(i-last_bad)
        return count