class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        l=[]

        for i in s:
            a= s.count(i)
            l.append(a)

        for j in range(len(l)):
            if l[0] != l[j]:
                return False

        return True


# Input: s = "aaabb"
# Output: false
# Input: s = "abacbc"
# Output: true
