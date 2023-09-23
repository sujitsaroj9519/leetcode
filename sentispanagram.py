class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        l = []

        for char in sentence:
            l.append(char)

        if len(set(l)) < 26:
            return False
        else:
            return True
        
obj = Solution()
print(obj.checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))
print(obj.checkIfPangram("leetcode"))