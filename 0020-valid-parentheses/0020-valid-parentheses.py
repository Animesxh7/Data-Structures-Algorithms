class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        mp = {')':'(','}':'{',']':'['}
        for i in s:
            if i in '({[':
                st.append(i)
            else:
                if not st or st[-1] != mp[i]:
                    return False
                st.pop()
        return len(st) == 0