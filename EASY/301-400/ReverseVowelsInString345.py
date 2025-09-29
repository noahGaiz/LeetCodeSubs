# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

# Example 1:

# Input: s = "IceCreAm"

# Output: "AceCreIm"

# Explanation:

# The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

# Example 2:

# Input: s = "leetcode"

# Output: "leotcede"
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = "aeiouAEIUO"
        s_ = list(s)
        start = 0
        end = len(s_) -1
        while start < end:
            if (s_[start] in vowels) and (s_[end] in vowels):
                s_[start], s_[end] = s_[end], s_[start]
                start+= 1
                end -= 1
            elif s_[start] in vowels:
                end -= 1
            elif s_[end] in vowels:
                start += 1
            else:
                start += 1
                end -= 1
        return "".join(s_)

                
