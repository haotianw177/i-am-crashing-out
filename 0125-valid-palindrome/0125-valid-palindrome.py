class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #use 2 pointers and build in function
        # first create 2 index varaibles at the begin and end of the screen
        
        l = 0 
        r = len(s) - 1
        # until 2 pointers meet in the middle
        while l < r:
            # if chracter at index l is not alphanumeric, increment
            if not s[l].isalnum():
                l += 1
            # if chracter at index r is not alphanumeric, decrement
            elif not s[r].isalnum():
                r -= 1
            # compare the l and r when they're lower, if same, move         left        and right pointer
            elif s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False
            
        return True
