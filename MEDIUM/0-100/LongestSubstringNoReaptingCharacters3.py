class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dc = {}
        res = 0
        left = 0
        right = 0
        while right < len(s):
            if s[right] not in dc:
                dc[s[right]] = 1
                right +=1
            else:
                del dc[s[left]]
                left += 1
                
            if res < right - left:
                res = right - left

        return res