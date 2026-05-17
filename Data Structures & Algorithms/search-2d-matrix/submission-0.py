class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if target > row[-1]:
                continue 
            else:
                for c in row:
                    if target == c:
                        return True
        return False