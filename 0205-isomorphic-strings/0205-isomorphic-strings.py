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

        for char_s, char_t in zip(s, t):
            # Check if there is an existing mapping for char_s in map_s_to_t
            if char_s in map_s_to_t:
                # If the mapped character doesn't match char_t, return False
                if map_s_to_t[char_s] != char_t:
                    return False
            else:
                map_s_to_t[char_s] = char_t

            # Similarly check for mapping from char_t to char_s
            if char_t in map_t_to_s:
                if map_t_to_s[char_t] != char_s:
                    return False
            else:
                map_t_to_s[char_t] = char_s

        return True