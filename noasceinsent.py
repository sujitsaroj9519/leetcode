class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        a = 0
        for i in s:
            if i.isdigit():
                if int(i) <= a:
                    return False
                else:
                    a = int(i)

        return True





        # b = 0
        # for i in s.split():
        #     if i.isdigit():
        #         if int(i) <= b:
        #             return False
        #         else:
        #             b = int(i)
        # return True







        # a = []

        # for i in s:
        #     if i.isdigit():
        #         a.append(int(i))

        # for j in range(1,len(a)):
        #     if a[j-1] < a[j]:
        #         return True
        #     else:
        #         return False
        # return a