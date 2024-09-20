class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        # seen = set()

        # for num in nums:
        #     if num in seen:
        #         return True
        #     seen.add(num)
        # return False

        # nums.sort()
        # n = len(nums)

        # for i in range (1, n):
        #     if nums[i] == nums[i - 1]:
        #         return True
        # return False
    
    
        # seen = {}
        # for num in nums:
        #     if num in seen:  # If the number has already been, return True
        #         return True
        #     seen[num] = 1  # Mark the number as seen
        # return False  

        deduplicated = set(nums)
        if len(deduplicated) != len(nums):
            return True
        return False