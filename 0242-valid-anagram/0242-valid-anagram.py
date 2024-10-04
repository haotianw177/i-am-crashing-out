class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        frequency = {}

        for i in s:
            if i in frequency:
                frequency[i] += 1
            else:
                frequency[i] = 1
        
        for i in t:
            if i in frequency:
                frequency[i] -= 1
            else:
                return False
        
        for i in frequency.values():
            # need to make sure i do not jump out of the loop early, so we use
            # != 0 here to loop through all elements, instead when i == 0 return  True, it could jump out of loop early 
            if i != 0:
                return False
        
        return True


    
        