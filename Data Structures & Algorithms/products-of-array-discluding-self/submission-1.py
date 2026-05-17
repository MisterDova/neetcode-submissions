import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        sol = []
        for i in range(len(nums)):
            val = 1
            arr = nums[:]
            arr.pop(i)
            for j in arr:
                val *= j
            sol.append(val)
        return sol