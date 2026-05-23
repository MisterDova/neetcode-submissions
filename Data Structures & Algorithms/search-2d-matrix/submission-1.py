class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if row[-1] < target:
                continue
            else:
                left = 0
                right = len(row) - 1
                while left <= right:
                    mid = ((right - left) // 2) + left
                    val = row[mid]
                    if target > val:
                        left = mid + 1
                    elif target < val:
                        right = mid - 1
                    else:
                        return True
        return False