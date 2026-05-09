class Solution:
    def encode(self, strs: list[str]) -> str:
        if not strs: return "EMPTY_LIST_SIGNAL" # Handle the [] case
        res = ""
        for s in strs:
            res += f"{s}#!$@"
        return res

    def decode(self, s: str) -> list[str]:
        if s == "EMPTY_LIST_SIGNAL": return []
        # split("#!$@") leaves an extra "" at the end, so we slice it off with [:-1]
        return s.split("#!$@")[:-1]