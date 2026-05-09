class Solution:
    def encode(self, strs: list[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> list[str]:
        #  4#neet5#co$de

        res, i = [], 0
        while i < len(s):
            j = i
            while s[j] != "#": # Find the end of the length number
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length]) # Slice exactly 'length' chars
            i = j + 1 + length # Jump to the start of the next block
        return res


'''
res = []
i = 0
j = 0

j = 1
length = 4

s[j + 1 : j + 1 + length] = n : t
res = [neet]
i = 6
---------------
res = [neet]
i = 6
j = 6

j = 7
length = 5

s[j + 1 : j + 1 + length] = c : e
res = [neet, co$de]
i = 13

'''