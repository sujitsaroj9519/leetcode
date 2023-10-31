class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        res = 0
        for i in words:
            if s.startswith(i):
                res +=1
        return res



        # c = 0
        # for i in words:
        #     n = len(i)
        #     if s[0:n] == i:
        #         c +=1
        # return c
        
# Input: words = ["a","b","c","ab","bc","abc"], s = "abc"
# Output: 3

# Input: words = ["a","b","c","ab","bc","abc"], s = "abc"
# Output: 3
# Input: words = ["a","a"], s = "aa"
# Output: 2