class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sPointer, tPointer = 0, 0
        # using i, which is iteration, will cause comparison of the elements of i at same index, but using pointer, which is 2 different elements, allow me to freely move one independant from another
        while tPointer < len(t) and sPointer < len(s):
            if s[sPointer] == t[tPointer]:
                sPointer += 1
            # we need to move tPointer regarldlessly if match
            tPointer += 1
        return sPointer == len(s)
# the idea is, the value of pointer of s move past s, which is index 3(start from 0 index 3 means a null ements), if equal to the length of s (3 because  not null and length start from 1) , return true, it's using the miss match of index numbers and lengeth numbers

        