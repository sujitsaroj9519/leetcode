class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        for r , c in zip(matrix, zip(*matrix)):
            if len(set(r)) != n or len(set(c)) != n:
                return False
        
        return True





        # n = len(matrix)
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[i])):
        #         for k in range(1,n+1):
        #             if k not in matrix[i]:
        #                 return False
        # return True



    
        
# Input: matrix = [[1,1,1],[1,2,3],[1,2,3]]
# Output: false

# Input: matrix = [[1,2,3],[3,1,2],[2,3,1]]
# Output: true