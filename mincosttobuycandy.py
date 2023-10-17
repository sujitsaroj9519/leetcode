class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        res = 0
        for i in range(len(cost)):
            if i %3 != len(cost)%3:
                res += cost[i]

        return res
        # s = 0
        # if len(cost) < 3:
        #     for i in cost:
        #         s += i
        #     return s
        

# Input: cost = [5,5]
# Output: 10

# Input: cost = [6,5,7,9,2,2]
# Output: 23


# Input: cost = [1,2,3]
# Output: 5