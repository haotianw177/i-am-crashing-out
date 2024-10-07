class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # we only need to check the lnegth of haystack till it exceed the possible contain length of needle
        # if needle = ha, haystack = haha, only check until the third h in haystack cuz the rest of won't fit needle which is ha
        for i in range(len(haystack) - len(needle) + 1):
            # Check if the substring of haystack matches the needle
            if haystack[i:i+len(needle)] == needle:
                return i  # Return the index of the first occurrence

        # If no match is found, return -1
        return -1
        