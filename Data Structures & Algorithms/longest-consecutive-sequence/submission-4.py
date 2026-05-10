class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # return if arr empty
        if not nums:
            return 0
        
        nums = sorted(set(nums))
        left = 0
        right = 1
        counts = []

        while right < len(nums):
            if nums[right] == nums[right - 1] + 1:
                right += 1
            else:
                counts.append(nums[left:right])
                left = right
                right += 1
        
        # Append last streak
        counts.append(nums[left:right])

        # Get longest sequence by length
        longest_seq = max(counts, key=len)
        return len(longest_seq)
