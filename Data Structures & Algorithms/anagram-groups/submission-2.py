class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = defaultdict(list)

        for s in strs:
            cout = [0] * 26

            for word in s:
                cout[ord(word) - ord("a")] += 1

            answer[tuple(cout)].append(s)
        return answer.values()