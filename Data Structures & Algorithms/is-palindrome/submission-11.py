class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""
        for c in s:
            if c.isalnum(): new_s += c.lower()
        
        left = 0
        right = len(new_s)-1
        
        while left <= right:
            print(left, right, new_s[left], new_s[right])
            if new_s[left] == new_s[right]:
                left += 1
                right -= 1
            else:
                return False
        
        return True