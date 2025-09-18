# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

 

# Example 1:

# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:

# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:

# Input: ransomNote = "aa", magazine = "aab"
# Output: true
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        dict1 = {}

    

        for i in ransomNote:

            if i not in dict1:

                dict1[i] = 1

            else:

                dict1[i]+=1

        for j in magazine:

            if j in dict1:

                dict1[j]-=1

        for i in dict1.values():

            if i>0:

                return False

        return True
 