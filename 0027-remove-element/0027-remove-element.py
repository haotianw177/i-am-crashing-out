class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k +=1
        return k
        # k acts as a barrier that separates valid elements (in the front) from elements that are still being processed., and we use i to check the loop, if the value if not equal to val(valid element), we move k(barrier) forward, and if the value is equal to val, we pause the k, and iterate i, and use the next i element to overwrite the the current k element, and then increment k


        