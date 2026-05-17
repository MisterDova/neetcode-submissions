class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        finder = {}
        for index, number in enumerate(nums):
            pending = target - number
            if pending in finder:
                return [finder[pending], index]
            finder[number] = index