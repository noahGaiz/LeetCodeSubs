class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        maxV = nums[0]
        minV = nums[0]
        

        for i in nums:
            if i > maxV:
                maxV = i

        for i in nums:
            if i < minV:
                minV = i

        breaks = 0

        for i in range(0,len(nums) -1):

            if nums[i] > nums[i+1]:
                

                if nums[i] == maxV and nums[i + 1] == minV:
                    breaks += 1
                else:
                    return False

        if nums[-1] > nums[0]:
            breaks += 1
        
        return breaks<=1
