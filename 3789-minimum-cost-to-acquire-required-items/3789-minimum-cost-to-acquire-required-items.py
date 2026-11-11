class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        cost = 0
        common = min(need1,need2)
        cost+=(common*min(costBoth,cost1+cost2))
        need1-=common
        need2-=common
        cost+=need1*min(costBoth,cost1)
        cost+=need2*min(costBoth,cost2)
        return cost