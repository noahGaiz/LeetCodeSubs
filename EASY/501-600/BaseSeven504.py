# Given an integer num, return a string of its base 7 representation.

 

# Example 1:

# Input: num = 100
# Output: "202"
# Example 2:

# Input: num = -7
# Output: "-10"
class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0: 
            return "0" 
            
        sign = '-' if num < 0 else '' 
        num = abs(num) 
        rem = [] 
        while num > 0: 
            rem.append(str(num % 7)) 
            num //= 7 
        return sign + ''.join(reversed(rem))
