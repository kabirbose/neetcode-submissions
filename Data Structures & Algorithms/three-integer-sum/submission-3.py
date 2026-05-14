class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums) # [-4, -1, -1, 0, 1, 2]
        curr = 0
        
        # We stop at len - 2 because we need room for left and right pointers
        while curr < len(nums) - 2:
            # DUPLICATE TRAP 1: If this number is same as the previous, skip it
            if curr > 0 and nums[curr] == nums[curr - 1]:
                curr += 1
                continue
                
            left = curr + 1
            right = len(nums) - 1
            
            while left < right:
                curr_sum = nums[curr] + nums[left] + nums[right]
                
                if curr_sum < 0:
                    left += 1
                elif curr_sum > 0:
                    right -= 1
                else:
                    # Triplet found!
                    res.append([nums[curr], nums[left], nums[right]])
                    
                    # DUPLICATE TRAP 2: Skip identical nums for left and right
                    # to avoid duplicate triplets in the result list
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    # Move both pointers to look for more pairs for this same 'curr'
                    left += 1
                    right -= 1
            
            # Only increment curr here at the bottom of the loop
            curr += 1

        return res

        