# Given two binary strings a and b, return their sum as a binary string.

 

# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if(a == '0'):
            return b
        if(b == '0'):
            return a

        while(len(a) != len(b)):
            if(len(a)< len(b)):
                a = "0" + a
            elif(len(a) > len(b)):
                b = "0" + b
            else:
                pass
        
        result = ''
        carry = 0
        for i in range(len(a) - 1, -1, -1):
            total = carry + int(a[i]) + int(b[i])
            result = str(total % 2) + result
            carry = total // 2

        if carry:
            result = '1' + result

        return result
        