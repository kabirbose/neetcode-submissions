class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        exists = set()

        for n in nums:
            if n in exists: return True
            else: exists.add(n)
        
        return False