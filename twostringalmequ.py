class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        c = set(word1+word2)

        for i in c:
            res = abs(word1.count(i) - word2.count(i)) >= 4
            if res:
                return False
        return True


# Input: word1 = "abcdeef", word2 = "abaaacc"
# Output: true

# Input: word1 = "aaaa", word2 = "bccb"
# Output: false