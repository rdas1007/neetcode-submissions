class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        M, N = len(matrix), len(matrix[0])
        l, r = 0, M*N - 1
        while l <= r:
            pivot = l + (r-l)//2
            col = pivot%N
            row = pivot//N
            if target == matrix[row][col]:
                return True 
            if target > matrix[row][col]:
                l = pivot + 1
            else:
                r = pivot - 1
        return False
            
                