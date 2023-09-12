class Solution:
    def findGCD(self, nums: List[int]) -> int:
        small = greatest = nums[0]
        for i in nums:
            if i < small:
                small = i
            if i > greatest:
                greatest = i

        while small and greatest:
            if greatest > small:
                greatest %= small
            else:
                small %= greatest

        return greatest if greatest > small else small




        # small = min(nums)
        # greatest = max(nums)

        # return gcd(small, greatest)



        # m = min(nums)
        # ma = max(nums)
        # if m % m ==0 and ma %m ==0:
        #     return m
        # else:
        #     return 1




        # Input: nums = [2,5,6,9,10]
        # Output: 2