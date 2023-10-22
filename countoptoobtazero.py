class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        # o = 0
        # while num1>0 and num2>0:
        #     if num1>num2:
        #         num1 -= num2
        #     else:
        #         num2 -= num1
        #     o +=1

        # return o




        o = 0
        while num1 > 0 and num2 > 0:
            if num1 > num2:
                num1 = num1 - num2
                # o +=1
            else: 
                num2 = num2 - num1
                # o +=1
            # elif num1 == num2:
            #     o +=1
            o +=1
        return o
        
# Input: num1 = 10, num2 = 10
# Output: 1

# Input: num1 = 2, num2 = 3
# Output: 3