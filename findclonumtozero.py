class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        a = []
        b = []

        for i in nums:
            if i > 0:
                a.append(i)
            else:
                b.append(i)
        
        a.sort()
        b.sort()
        if len(a)==0:
            return b[-1]
        elif len(b)==0:
            return a[0]
        elif abs(0-a[0]) > abs(0-b[-1]):
            return b[-1]
        elif abs(0-a[0]) < abs(0-b[-1]):
            return a[0]
        else:
            return a[0]




        # l = []
        # for i in nums:
        #     l.append(0 - i)
        # m = min(l)
        # for j in range(len(l)):
        #     if m == l[j]:
        #         return nums[j]
        #     break
        

#         Input: nums = [2,-1,1]
# Output: 1

# Input: nums = [-4,-2,1,4,8]
# Output: 1