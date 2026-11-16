class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s)>k:
            res = ""
            for i in range(0,len(s),k):
                a = s[i:i+k]
                sumi = 0
                for i in range(len(a)):
                    sumi += int(a[i])
                res+=str(sumi)
            s = res
        return s
        
        
        
