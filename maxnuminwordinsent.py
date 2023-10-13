class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        n = 0
        l = []
        for i in sentences:
            for j in i.split(" "):
                n +=1

            l.append(n)
            n = 0
        return max(l)
        

# Input: sentences = ["please wait", "continue to fight", "continue to win"]
# Output: 3

# Input: sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
# Output: 6