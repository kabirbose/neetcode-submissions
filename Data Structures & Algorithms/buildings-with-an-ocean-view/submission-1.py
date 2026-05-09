class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        indices = [len(heights)-1]

        for i in reversed(range(len(heights)-1)):
            if heights[i] > heights[indices[-1]]:
                indices.append(i)
        
        return indices[::-1]
        