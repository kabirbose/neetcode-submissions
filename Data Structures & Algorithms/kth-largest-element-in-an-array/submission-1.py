class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        count = 1

        hashmap = {} #kth largest, val

        while nums:
            hashmap[count] = max(nums)
            nums.remove(max(nums))
            count +=1

        return hashmap[k]