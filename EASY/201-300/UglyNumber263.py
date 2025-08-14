# An ugly number is a positive integer which does not have a prime factor other than 2, 3, and 5.

# Given an integer n, return true if n is an ugly number.

 

# Example 1:

# Input: n = 6
# Output: true
# Explanation: 6 = 2 × 3
# Example 2:

# Input: n = 1
# Output: true
# Explanation: 1 has no prime factors.
# Example 3:

# Input: n = 14
# Output: false
# Explanation: 14 is not ugly since it includes the prime factor 7.

class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        true2 = True
        true3 = True
        true5 = True
        while n > 0:
            while true2:
                if n % 2 == 0:  
                    n //= 2
                else:
                    true2 = False

            while true3:
                if n % 3 == 0:
                    n //= 3
                else:
                    true3 = False

            while true5:
                if n % 5 == 0:
                    n //= 5
                else:
                    true5 = False

            return n == 1
        return n == 0

