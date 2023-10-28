class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        l1, l2, l3 = [], [], []
        for i in nums1:
            if i in nums2:
                continue
            else:
                l2.append(i)
        for j in nums2:
            if j in nums1:
                continue
            else:
                l3.append(j)
        l1.append(list(set(l2)))
        l1.append(list(set(l3)))
        return l1




        # l1 = set(nums1)
        # l2 = set(nums2)
        # return [list(l1-l2), list(l2-l1)]

obj = Solution()
print(obj.findDifference([1,2,3,3],[1,1,2,2]))
        
# Input: nums1 = [1,2,3,3], nums2 = [1,1,2,2]
# Output: [[3],[]]

# Input: nums1 = [1,2,3], nums2 = [2,4,6]
# Output: [[1,3],[4,6]]