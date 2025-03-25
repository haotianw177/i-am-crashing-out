class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        pre = ""
        result = []

        # This loop goes from the last character of s to the first. The range function starts at len(s) - 1 (the last index) and decrements by 1 until it reaches 0.
        for i in range(len(s) - 1, -1, -1):
            # Check for a Space
            if s[i] == " ":
                # Before doing anything, it checks if pre is not empty. This ensures that we only act when we have actually accumulated a word.
                if pre != "":
                    result.append(pre)
                    pre = ""
            else:
                # The current character s[i] is added to the beginning of pre.
                pre = s[i] + pre
                    
                
        if pre != "":
                # After the loop, if pre is not empty, it means there is one last word that hasn't been added to the list (this happens if the string does not end with a space).
            result.append(pre)
        
        return " ".join(result)
        # The list of words in result is joined together into a single string, with a space inserted between each word. This final string is then returned.



        