class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        res = ''
        for char in word:
            if char.isdigit():
                res = res + char
            else:
                res = res + ' '

        res = res.split(' ')

        # return len(set(res))-1
        out = []

        for num in res:
            if num != '':
                out.append(int(num))

        return len(set(out))
        # return res
        
obj = Solution()
print(obj.numDifferentIntegers("a123bc34d8ef34"))
print(obj.numDifferentIntegers("leet1234code234"))
print(obj.numDifferentIntegers("a1b01c001"))