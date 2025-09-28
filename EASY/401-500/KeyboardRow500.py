# Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.

# Note that the strings are case-insensitive, both lowercased and uppercased of the same letter are treated as if they are at the same row.

# In the American keyboard:

# the first row consists of the characters "qwertyuiop",
# the second row consists of the characters "asdfghjkl", and
# the third row consists of the characters "zxcvbnm".

 

# Example 1:

# Input: words = ["Hello","Alaska","Dad","Peace"]

# Output: ["Alaska","Dad"]

# Explanation:

# Both "a" and "A" are in the 2nd row of the American keyboard due to case insensitivity.

# Example 2:

# Input: words = ["omk"]

# Output: []

# Example 3:

# Input: words = ["adsdf","sfd"]

# Output: ["adsdf","sfd"]
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        
        top = set("qwertyuiop")
        mid = set("asdfghjkl")
        bot = set("zxcvbnm")
        inter = []
        for word in words:
            c1 = 0
            c2 = 0
            c3 = 0
            for val in word.lower():
                if val in top:
                    c1 += 1
                if val in mid:
                    c2 += 1
                if val in bot:
                    c3 += 1
            if c1 == len(word) or c2 == len(word) or c3 == len(word):
                inter.append(str(word))
        return inter
        