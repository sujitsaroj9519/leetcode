class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        c = 0
        for i in range(len(patterns)):
            if patterns[i] in word:
                c +=1
        return c

obj = Solution()
print(obj.numOfStrings(["a","abc","bc","d"],"abc"))

# Input: patterns = ["a","abc","bc","d"],
# word = "abc"
# Output: 3