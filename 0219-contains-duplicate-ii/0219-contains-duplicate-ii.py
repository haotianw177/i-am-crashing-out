class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        dict ={}

        for idx in range(len(nums)):
            if nums[idx] in dict and abs(idx- dict[nums[idx]]) <=k:
                return True
            dict[nums[idx]] = idx
        return False
        