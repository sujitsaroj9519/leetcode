class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        c = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if abs(nums[i] - nums[j]) == k:
                    c +=1
        return c
    
obj = Solution()
print(obj.countKDifference(nums = [3,2,1,5,4], k = 2))





# Input: nums = [1,2,2,1], k = 1
# Output: 4

# Input: nums = [1,3], k = 3
# Output: 0

# Input: nums = [3,2,1,5,4], k = 2
# Output: 3
        