class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        w1 = words1
        w2 = words2
        c = 0
        for i in w1:
            if w1.count(i) == w2.count(i) ==1:
                c +=1
        return c




        # c = 0
        # for i in words1:
        #     if words1.count(i) == 1 and words2.count(i) == 1 and i in words2:
        #         print(i)
        #         c +=1
        # return c
        
        
# Input: words1 = ["leetcode","is","amazing","as","is"], words2 = ["amazing","leetcode","is"]
# Output: 2

# Input: words1 = ["b","bb","bbb"], words2 = ["a","aa","aaa"]
# Output: 0
