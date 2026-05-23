class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = ((right - left) // 2) + left
            val = nums[mid]
            if target > val:
                left = mid + 1
            elif target < val:
                right = mid - 1
            else:
                return mid
        return -1