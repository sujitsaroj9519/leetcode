class Solution:
    def countElements(self, nums: List[int]) -> int:
        nums.sort()
        m = nums.count(min(nums))
        ma = nums.count(max(nums))

        if len(nums) == 1:
            return 0 
        elif min(nums) == max(nums):
            return 0
        else:
            return len(nums) - m -ma


        # c = 0

        # for i in nums:
        #     if i != m or i != ma:
        #         c +=1
        # return c-2
       

# Input: nums = [-3,3,3,90]
# Output: 2

# Input: nums = [11,7,2,15]
# Output: 2