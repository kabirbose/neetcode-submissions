class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)))
        res = []
        
        start = 0
        left = 0
        right = 1
        
        while(right < len(nums)):
            if nums[left] == nums[right]-1:
                left += 1
                right += 1
            else:
                res.append(nums[start:left+1])
                left += 1
                right += 1
                start = left
        
        res.append(nums[start:right+1])
        
        return len(max(res, key=len))