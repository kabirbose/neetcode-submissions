class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        stored_nums = {}

        for i, n in enumerate(nums):
            diff = target - n

            if diff in stored_nums:
                return [stored_nums[diff], i]
            stored_nums[n] = i
        return
        