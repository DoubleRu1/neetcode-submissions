class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = -1, m*n
        while left < right - 1:
            mid = (left + right) // 2
            i, j = mid // n, mid % n
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                left = mid
            else:
                right = mid
    
        return False