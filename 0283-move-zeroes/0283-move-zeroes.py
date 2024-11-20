class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[right], nums[left] = nums[left], nums[right]
                left += 1
        return nums

# The left pointer guarantees the boundary between non-zero and zero elements.
# The right pointer simply iterates, finding non-zero elements and swapping them into their correct position (defined by left).
# At the end, all zeros are moved to the right, and non-zero elements remain in their original relative order.

        