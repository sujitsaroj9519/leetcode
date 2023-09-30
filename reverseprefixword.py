class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        for i in range(len(word)):
            if word[i] == ch:
                return word[:i+1][::-1] + word[i+1:]

        return word
        
        # if ch not in word:
        #     return word
        
        # ind = list(word).index(ch)
        # l =(word[:ind+1][::-1])
        # word = list(word)
        # word[:ind+1] = l

        # return ''.join(word)

obj = Solution()
print(obj.reversePrefix( word = "abcdefd", ch = "d"))