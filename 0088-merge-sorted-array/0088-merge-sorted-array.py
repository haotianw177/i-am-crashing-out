class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        #so you're saying, j is only index value, which is numerical, when adding j to m, which m also is numerial, is ok? for example, the first itertation, m is at 3 because only 3 numbers in num1, and j is starting at 0, 3+0 =3, which means that at the index 3 , which is the 4th element in nums 1, put in the index 0 element of j, which is 4?
        for j in range(n):
            nums1[m+j] = nums2[j]
        nums1.sort()
        #this apporach just addpend the nums2 to end of nums1
        