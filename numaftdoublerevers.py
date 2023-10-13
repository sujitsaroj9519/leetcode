class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        num = str(num)
        re = num[::-1]
        re = int(re)
        re1 = str(re)[::-1]

        return int(num) == int(re1)
        


# Input: num = 0
# Output: true

# Input: num = 1800
# Output: false

# Input: num = 526
# Output: true