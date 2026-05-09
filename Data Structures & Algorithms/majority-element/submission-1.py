class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}

        for i, n in enumerate(nums):
            if n not in hashmap:
                hashmap[n] = 1
            else:
                hashmap[n] += 1

        for k, v in hashmap.items():
            if v > len(nums)/2:
                return k
        