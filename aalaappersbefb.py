class Solution:
    def checkString(self, s: str) -> bool:
        c = s[0]
        if s[0] =="b" and "a" in s:
            return False

        for i in range(len(s)):
            if c == s[i]:
                continue
            elif c in s[i+1:]:
                return False

        return True

        

# Input: s = "bbb"
# Output: true

# Input: s = "abab"
# Output: false

# Input: s = "aaabbb"
# Output: true