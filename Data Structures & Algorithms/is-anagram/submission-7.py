class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hashmap = {}
        t_hashmap = {}

        for c in s:
            if c not in s_hashmap: s_hashmap[c] = 1
            else: s_hashmap[c] += 1

        for c in t:
            if c not in t_hashmap: t_hashmap[c] = 1
            else: t_hashmap[c] += 1
        
        if s_hashmap == t_hashmap: return True
        return False