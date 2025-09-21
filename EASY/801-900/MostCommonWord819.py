# Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique.

# The words in paragraph are case-insensitive and the answer should be returned in lowercase.

# Note that words can not contain punctuation symbols.

 

# Example 1:

# Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
# Output: "ball"
# Explanation: 
# "hit" occurs 3 times, but it is a banned word.
# "ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
# Note that words in the paragraph are not case sensitive,
# that punctuation is ignored (even if adjacent to words, such as "ball,"), 
# and that "hit" isn't the answer even though it occurs more because it is banned.
# Example 2:

# Input: paragraph = "a.", banned = []
# Output: "a"

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        para = re.findall(r"[a-zA-Z]+", paragraph.lower())
        paragraph = paragraph.lower().split()
        
        dc = {}
        highest = 0
        res = ''
        for i in para:
            if i in dc:
                dc[i] += 1
            else:
                dc[i] = 1
        
        for n, p in dc.items():
            if n not in banned and p > highest:
                highest = p
                res = n
        return res
            
