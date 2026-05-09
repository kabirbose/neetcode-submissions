class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        indices = []

        for i in range(len(heights)-1):
            
            if heights[i] > max(heights[i+1:]):
                indices.append(i)

        indices.append(len(heights)-1)

        return indices
        