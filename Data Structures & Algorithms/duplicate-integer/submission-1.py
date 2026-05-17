class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checker = {}
        for numbers in nums:
            if numbers in checker:
                return True
            else:
                checker[numbers] = 1
        return False