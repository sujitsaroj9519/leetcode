class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        max_dis = 0
        for i in range(len(colors)):
            for j in range(len(colors)):
                if colors[i] != colors[j]:
                    max_dis = max(max_dis, abs(j-i))

        return max_dis



        # i = 0
        # l = len(colors)
        # j = l-1

        # while colors[j] == colors[0]:
        #     j -=1
        # while colors[-1] == colors[i]:
        #     i +=1

        # return max(j,l-1-i)


        # ind1 = 0
        # ind2 = -1
        # size = len(colors)

        # while ind1< size:
        #     front = colors[ind1]

        #     if front != colors[-1]:
        #         return size-ind1-1

        #     last = colors[ind2]

        #     if last != colors[0]:
        #         return size + ind2

        #     ind1 +=1
        #     ind2 -=1







        # m = min(colors)
        # ma = max(colors)
        # a = 0
        # b = 0

        # for i in  range(len(colors)):
        #     if m == colors[i]:
        #         a = i
        #         break
        #     if ma == colors[j]:
        #         b =i 
        #         break

        # return abs(a-b)

        