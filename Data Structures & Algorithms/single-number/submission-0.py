class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = {}
        for n in nums:
            if n not in res:
                res[n] = 1
            else:
                res.pop(n)
        for num, cout in res.items():
            return num