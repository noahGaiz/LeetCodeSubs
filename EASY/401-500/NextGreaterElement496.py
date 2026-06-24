class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        lol = [-1] * len(nums1)
        for i in range(len(nums1)):
            k = False
            for j in nums2:
                if nums1[i] == j:
                    k=True
                elif k and j>nums1[i]:
                    lol[i] = j
                    break
        return lol