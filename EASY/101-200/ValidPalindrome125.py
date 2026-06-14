
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
    
        res = ""
        for ch in s:
            if ch.isalnum():
                res += ch.lower()

        return res == res[::-1]