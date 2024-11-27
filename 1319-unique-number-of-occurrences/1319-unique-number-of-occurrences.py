class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        
        hashMap ={}

        for i in arr:
            if i in hashMap:
                hashMap[i] += 1
            else:
                hashMap[i] = 1
        return len(hashMap.values()) == len(set(hashMap.values()))
        # if total numer of elements account equal to unique counts, no duplicate
        

        