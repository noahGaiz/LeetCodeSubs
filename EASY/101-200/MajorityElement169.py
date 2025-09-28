# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mx = 0
        dc = {}
        for i in nums:
            if i in dc:
                dc[i] += 1
            else:
                dc[i] = 1
        for y in dc.values():
            if y > mx:
                mx = y
        for x,y in dc.items():
            if y == mx:
                return x
        return -1
