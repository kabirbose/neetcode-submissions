class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        output = []
        
        for i in range(len(strs)):
            if "".join(sorted(strs[i])) not in hashmap:
                hashmap["".join(sorted(strs[i]))] = [strs[i]]
            else:
                hashmap["".join(sorted(strs[i]))].append(strs[i])
        
        for k, v in hashmap.items(): output.append(v)
        
        return output
        