class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        
        while left < right:
            # check if already palindrome by checking pointers are equal value
            # outer return True will execute
            if s[left] == s[right]:
                left +=1
                right -=1
            
            # if while loop doesnt break, not palindrome
            else:
                removed_l = s[left+1:right+1]
                removed_r = s[left:right]
                
                # this checks the splice and returns False if conditions neither is matched
                return (removed_l == removed_l[::-1] or removed_r == removed_r[::-1])
        
        return True