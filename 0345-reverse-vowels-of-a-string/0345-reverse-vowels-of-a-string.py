class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        n = len(s)
        l, r = 0, n - 1
        s = list(s)
        vowels = list("aeiouAEIOU")

        # Strings in Python cannot(immutable) be changed directly after they are created
        # Since reversing vowels requires swapping characters (i.e., modifying specific positions in the string), the solution converts the string into a list where individual elements (characters) can be changed.

        # `l` is the left pointer to track the vowel character
        # `r` is the right pointer to track the vowel character
        while l < r:
            # find the index of the first vowel in the given range
            while l < r and s[l] not in vowels:
                l += 1
            # find the index of last vowel in the given range
            while r > l and s[r] not in vowels:
                r -= 1
            # swap s[l] and s[r]
            s[l], s[r] = s[r], s[l]
            # since we've processed the character s[l],
            # we move the left pointer to the right
            l += 1
            # since we've processed the character s[r],
            # we move the right pointer to the left
            r -= 1
            
        return "".join(s)
        