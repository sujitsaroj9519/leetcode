class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            news = ''
            for i in range(0,len(s),k):
                temp = 0
                for d in s[i:i+k]:
                    temp += int(d)

                news += str(temp)
            s = news
        return s

        
        # s = list(map(int,s))
        # while len(s) > k:
        #     temp = []

        #     for i in range(0,len(s),k):
        #         S = sum(s[i:i+k])
        #         for d in (str(S)):
        #             temp.append(int(d))

        #     s =temp

        # return ''.join(map(str,s))
    
#     Input: s = "11111222223", k = 3
# Output: "135"

# Input: s = "00000000", k = 3
# Output: "000"