# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true

# Example 2:

# Input: s = "rat", t = "car"

# Output: false

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        dc = {}
        
        
        for i in s:
            dc[i] = dc.get(i, 0) +1
        for i in t:
            if i not in dc:
                return False
            dc[i] -= 1 
            if dc[i] < 0: 
                return False
        return True
        # return sorted(s) == sorted(t)
        