# A word is considered valid if:

# It contains a minimum of 3 characters.
# It contains only digits (0-9), and English letters (uppercase and lowercase).
# It includes at least one vowel.
# It includes at least one consonant.
# You are given a string word.

# Return true if word is valid, otherwise, return false.

# Notes:

# 'a', 'e', 'i', 'o', 'u', and their uppercases are vowels.
# A consonant is an English letter that is not a vowel.
 

# Example 1:

# Input: word = "234Adas"

# Output: true

# Explanation:

# This word satisfies the conditions.

# Example 2:

# Input: word = "b3"

# Output: false

# Explanation:

# The length of this word is fewer than 3, and does not have a vowel.

# Example 3:

# Input: word = "a3$e"

# Output: false

# Explanation:

# This word contains a '$' character and does not have a consonant.

class Solution(object):
    def isValid(self, word):
        """
        :type word: str
        :rtype: bool
        """
        worded = word.lower()
        length = False
        hasDig = False
        hasVow = False
        hasCos = False
        digits = '0123456789'
        vowels = 'aeiou'
        consonant = 'qwrtypsdfghjklzxcvbnm'

        if len(worded)>= 3:
            length = True
        else:
            return False

        for letter in worded:
            if letter in digits:
                hasDig = True
            elif letter in vowels:
                hasVow = True
            elif letter in consonant:
                hasCos = True
            else:
                return False

        return(length and hasCos and hasVow)