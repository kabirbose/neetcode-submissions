class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for i, n in enumerate(nums):
            if n not in freq:
                freq[n] = 0
            else:
                freq[n] += 1

        output = sorted(freq, key=freq.get, reverse=True)[:k]
        return output


        