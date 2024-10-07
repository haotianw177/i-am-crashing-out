class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Create two dictionaries to store mappings
        map_s_to_t = {}
        map_t_to_s = {}


        # Zip is part of a loop that iterates over two strings (s and t) simultaneously. zip is a Python     built-in function that takes two or more iterables (like strings, lists, etc.) and "zips" them together.
        for char_s, char_t in zip(s, t):
            # Check if there is an existing mapping for char_s in map_s_to_t
            if char_s in map_s_to_t:
                # If the mapped character doesn't match char_t, return False
                if map_s_to_t[char_s] != char_t:
                    return False
            else:
                map_s_to_t[char_s] = char_t

            # Similarly check for mapping from char_t to char_s
            # why do need reverse check? let's say s=ab, t=cc
            if char_t in map_t_to_s:
                if map_t_to_s[char_t] != char_s:
                    return False
            else:
                map_t_to_s[char_t] = char_s

            # Forward check (s -> t) ensures that each character in s consistently maps to one character in t. Reverse check (t -> s) ensures that no two characters from s map to the same character in t.

        return True