class Solution:
    def arraySign(self, nums: List[int]) -> int:
      
        x = nums[0]
        for i in range(1,len(nums)):
            x *= nums[i]

        if x < 0 :
            return -1
        elif x > 0:
            return 1
        else:
            return 0
        
