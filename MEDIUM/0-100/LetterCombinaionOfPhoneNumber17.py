class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dc = {}
        res = [""]
        letters = ""
        dc[2] = "abc"
        dc[3] = "def"
        dc[4] = "ghi"
        dc[5] = "jkl"
        dc[6] = "mno"
        dc[7] = "pqrs"
        dc[8] = "tuv"
        dc[9] = "wxyz"
        
        if digits == "":
            return []

        for dig in digits:
            newRes = []
            letters += dc[int(dig)]
            for exis in res:
                for let in letters:
                    newRes.append(exis + let)
            res = newRes
            letters = ""

        return res