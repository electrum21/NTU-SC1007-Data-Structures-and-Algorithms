# You are given an integer array nums of length n. 
# A neighbour of an element nums[i] refers to the adjacent elements nums[i-1] and nums[i+1] (if they exist). 
# An element nums[i] is called a peak element if it is strictly greater than its neighbours.
# For convenience, assume that nums[-1] = nums[n] = -infinity. You may assume at least one peak element always exists in the array.
# Design an algorithm to find the index of any peak element in O(log n) time.


class Solution:
    def find_peak(self, nums):
        #nums: an array.
        # Returns:
        # peak_index: The index of the peak element.
        
        # Initialize left and right pointers
        left, right = 0, len(nums) - 1
        
        while left < right:
            # Find the mid index
            mid = (left + right) // 2
            
            # Compare nums[mid] with nums[mid + 1]
            if nums[mid] < nums[mid + 1]:
                # Move the left pointer to mid + 1
                left = mid + 1
            else:
                # Move the right pointer to mid
                right = mid
        
        # The peak index is left when left == right
        return left