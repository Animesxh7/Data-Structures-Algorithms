class ProductOfNumbers:
    def __init__(self):
        self.a = [1]
    def add(self, num: int) -> None:
        if num == 0:
            self.a = [1]
        else:
            self.a.append(self.a[-1]*num)
    def getProduct(self, k: int) -> int:
        if k>=len(self.a):
            return 0
        return self.a[-1]//self.a[-k-1]


        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)