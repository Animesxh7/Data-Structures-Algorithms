class Solution:
    def addDigits(self, num: int) -> int:
        a = str(num)
        while num>9:
            sumi = 0
            while num>0:
                sumi+=(num%10)
                num//=10
            num = sumi
        return num