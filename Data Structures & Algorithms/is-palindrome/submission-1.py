class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""
        
        for i in range(len(s)):
            if s[i].isalnum():
                new_s += s[i].lower()
        
        if new_s[::-1] == new_s:
            return True
        else:
            return False
        