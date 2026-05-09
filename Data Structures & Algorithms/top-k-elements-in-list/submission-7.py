class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        output = []

        for i in range(len(nums)):
            if nums[i] not in hashmap: hashmap[nums[i]] = 1
            else: hashmap[nums[i]] += 1
        
        count = 0
        for num, freq in sorted(hashmap.items(), key=lambda item: item[1], reverse=True):
            # print(num, freq)
            output.append(num)
            count += 1

            if count == k: return output