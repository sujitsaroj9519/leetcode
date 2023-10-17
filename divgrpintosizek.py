class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        l =[]
        for i in range(0,len(s),k):
            l.append(s[i:i+k])
        l1 =[]
        for j in l:
            if len(j)==k:
                l1.append(j)
            else:
                j += fill* (k-len(j))
                l1.append(j)

        return l1


# Input: matrix = [[1,1,1],[1,2,3],[1,2,3]]
# Output: false

# Input: matrix = [[1,2,3],[3,1,2],[2,3,1]]
# Output: true

