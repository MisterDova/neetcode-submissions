class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        output = []
        for i in nums:
            if i not in res:
                res[i] = 1
            else:
                res[i] += 1
        
        res = list(sorted(res.items(), key=lambda x: x[1], reverse=True))
        for i in range(k):
            output.append(res[i][0])
        return output