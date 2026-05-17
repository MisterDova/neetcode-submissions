class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        size = len(nums)
        for i in range(size):
            res = 1
            for j in range(size):
                if i == j:
                    continue
                res *= nums[j]
            output.append(res)
        return output