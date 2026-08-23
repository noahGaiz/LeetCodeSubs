class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        res = ""
        currRow = 0
        step = 0
        secStep = 0
        cycle = 2* (numRows - 1)
        if numRows == 1:
            return s

        
        for currRow in range(numRows):
            if (currRow == 0) or (currRow == numRows -1):
                step = 2* (numRows - 1)
            else:
                step = 2 * (numRows - currRow - 1)
                secStep = cycle - step

            
            if (currRow == 0) or (currRow == numRows -1):
                for char in range(currRow,len(s),step):
                    res += s[char]
            else:
                char = currRow
                while char < len(s):
                    res += s[char]
                    char+= step
                    if char >= len(s):
                        break

                    res += s[char]
                    char += secStep

        return res
        