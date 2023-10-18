class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        # odd = list()
        # even = list()
        # res = list()

        # for i in range(len(nums)):
        #     if i %2:
        #         odd.append(nums[i])
        #     else:
        #         even.append(nums[i])

        # odd = sorted(odd, reverse= True)
        # even = sorted(even)

        # for j in range(len(odd)):
        #     res.append(even[j])
        #     res.append(odd[j])

        # for i in nums:
        #     if nums.count(i) != res.count(i):
        #         res.append(i)
        # return res





        e = []
        o = []
        for i in range(len(nums)):
            if i % 2 :
                o.append(nums[i])
            else:
                e.append(nums[i])

        e.sort()
        o.sort(reverse = True)
        l = []
        for i in range(len(o)):
            l.append(e[i])
            l.append(o[i])
        
        for j in nums:
            if nums.count(j) != l.count(j):
                l.append(j)
        
        return l
        
        
# Input: nums = [2,1]
# Output: [2,1]

# Input: nums = [4,1,2,3]
# Output: [2,3,4,1]