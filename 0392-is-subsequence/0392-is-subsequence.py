class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        i, j = 0, 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        
        return i == len(s)

        
        
# i	j	s[i]	t[j]	Match?	i After	j After
# 0	0	a	    a	    ✅ Yes	1	    1
# 1	1	b	    h	    ❌ No	1	    2
# 1	2	b	    b	    ✅ Yes	2	    3
# 2	3	c	    g	    ❌ No	2	    4
# 2	4	c	    d	    ❌ No	2	    5
# 2	5	c	    c	    ✅ Yes	3	    6