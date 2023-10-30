class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        a= []
        s = sorted(nums)
        for i in s[0]:
            cou= 1
            for j in s[1:]:
                if i not in j:
                    cou= 0
                    break
            if cou:
                a.append(i)
        return sorted(a)


        # a = []
        # for i in nums[0]:
        #     for j in nums[1:]:
        #         if i not in j:
        #             # a.append(i)
        #             break
        #     a.append(i)
        
        # return a
        
        
# Input: nums = [[1,2,3],[4,5,6]]
# Output: []

# Input: nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]
# Output: [3,4]