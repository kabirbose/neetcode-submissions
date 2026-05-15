class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights)-1
        curr_max = 0
        
        while j > i:
            area = min(heights[i], heights[j]) * (j-i)
            curr_max = max(curr_max, area)
            
            if heights[i] < heights[j]: i += 1
            elif heights[i] > heights[j]: j -= 1
            else: i += 1
        
        return curr_max