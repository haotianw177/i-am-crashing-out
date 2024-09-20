class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        end = len(s)- 1
        
        # this while loop will keep on running
        while s[end] == " ":
            end -= 1

        start = end
        # this while loop will keep on running
        while start >= 0 and s [start]!= " ":
            start -= 1

        return end - start