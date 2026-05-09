class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        for i in range(len(strs[0])): #loop through "bat"
            for s in strs: #now loop through all items in strs len(strs[0]) -> 3 times
                #if i = out of bounds OR curr char of curr str != curr char of "bat"
                if i==len(s) or s[i] != strs[0][i]:
                    return res;
            
            res +=strs[0][i]

        return res
        