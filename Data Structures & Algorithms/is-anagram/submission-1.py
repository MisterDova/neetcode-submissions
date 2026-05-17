class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_check = {}
        t_check = {}
        
        for c in s:
            if c not in s_check:
                s_check[c] = 1
            else:
                s_check[c] += 1
        
        for c in t:
            if c not in t_check:
                t_check[c] = 1
            else:
                t_check[c] += 1
        
        return s_check == t_check