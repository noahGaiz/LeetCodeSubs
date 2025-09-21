# You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

# You are given an integer array nums representing the data status of this set after the error.

# Find the number that occurs twice and the number that is missing and return them in the form of an array.

 

# Example 1:

# Input: nums = [1,2,2,4]
# Output: [2,3]
# Example 2:

# Input: nums = [1,1]
# Output: [1,2]

class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        cet = set()
        result = []

        dup = 0
        for i in nums:
            if i in cet:
                dup = i
            cet.add(i)

        miss = 0
        for i in range(1, len(nums) + 1):
            if i not in cet:
                miss = i
                break
        result.append(dup)
        result.append(miss)
        return result
