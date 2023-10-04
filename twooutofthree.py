class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        ans = []
        for i in nums1:
            if i in nums2 or i in nums3:
                if i not in ans:
                    ans.append(i)

        for j in nums2:
            if j in nums3 or j in nums1:
                if j not in ans:
                    ans.append(j)

        return ans



        # return set(nums1) & set(nums2) | set(nums2) & set(nums3) | set(nums1) & set(nums3)







        # a = []
        # l1 = len(nums1)
        # l2 = len(nums2)
        # l3 = len(nums3)

        # if l1 == l2 == l3:
        #     for i in nums1:
        #         if i in nums2 or i in nums3:
        #             a.append(i)
        #     for i in nums2: 
        #         if i in nums3:
        #             a.append(i)

        # elif l1 >= l2 and l1 >= l3:
        #     for i in nums1 :
        #         if ( i in nums2 ) or (i in nums3) :
        #             a.append(i)

        # elif l2 >= l1 and l2 >=l3:
        #     for i in nums2:
        #         if ( i in nums1 ) or (i in nums3) :
        #             a.append(i)

        # elif l3 >= l2 and l3 >=l1:
        #     for i in nums3:
        #         if  (i in nums1 ) or (i in nums2) :
        #             a.append(i)

        

        # return list(set(a))