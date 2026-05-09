class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashmap = {}
        output = []

        for val in strs:
            sorted_val = "".join(sorted(val))
            if sorted_val not in hashmap: hashmap[sorted_val] = [val]
            else: hashmap[sorted_val].append(val)

        for k, v, in hashmap.items():
            output.append(v)
        
        return output