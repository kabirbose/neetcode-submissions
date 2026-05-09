class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        output = []

        for c in strs:
            sorted_c = "".join(sorted(c))
            
            if sorted_c not in hashmap:
                hashmap[sorted_c] = [c]
            else:
                hashmap[sorted_c].append(c)

        for k,v in hashmap.items():
            output.append(v)
        
        return output