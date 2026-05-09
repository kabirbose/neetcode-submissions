class Solution:
    def productExceptSelf(self, nums):
        curr = 1
        new_arr = []

        while curr < len(nums)+1:
            prefix_arr = nums[0:curr-1]
            postfix_arr = nums[curr:len(nums)]
            
            prefix = 1
            postfix = 1
            
            for n in prefix_arr: prefix *= n
            for n in postfix_arr: postfix *=n
            new_arr.append(prefix * postfix)
            curr+=1
        
        return new_arr