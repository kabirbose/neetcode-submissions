class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        duplicates = set()

        for i, n in enumerate(nums):
            if n not in duplicates:
                duplicates.add(n)
            else:
                return True
        
        return False
        