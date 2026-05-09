class Solution:
    def productExceptSelf(self, nums):
        res = []

        for i in range(len(nums)):
            curr = nums[i]
            nums[i] = 1
            
            res.append(math.prod(nums))
            
            nums[i] = curr
        
        return res