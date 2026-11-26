class Solution:
    def canAliceWin(self, n: int) -> bool:
        if (n>9 and n<=18) or (n>26 and n<=33) or (n>39 and n<=44) or n>48:
            return True
        return False
        


