class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniqueNums = set()

        for n in nums:
            if n not in uniqueNums:
                uniqueNums.add(n)
            else:
                return True
        
        return False

        
        