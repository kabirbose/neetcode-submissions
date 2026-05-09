class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        duplicates = []

        for i, n in enumerate(nums):
            if n not in duplicates:
                duplicates.append(n)
            else:
                return True
        
        return False
        