class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for i in words:
            if i == i[::-1]:
                return i

        return ""
        

# Input: words = ["def","ghi"]
# Output: ""

# Input: words = ["notapalindrome","racecar"]
# Output: "racecar"

# Input: words = ["abc","car","ada","racecar","cool"]
# Output: "ada"