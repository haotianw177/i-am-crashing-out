class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # no defaultdict: for num in nums:
        # if num in m:
        #     m[num] += 1
        # else:
        #     m[num] = 1 
        # Manually initialize the count to 1 when the key doesn't exist

        # n = len(nums)
        # map = defaultdict(int)

        # # Count the occurrences of each number
        # for num in nums:
        #     # If the key doesn't exist,initialized to 0 and then incremented
        #       map[num] += 1  
        
        # n = n // 2
        # for key, value in map.items():
        #     if value > n:
        #         return key
        
        # return 0



        # Since the list is sorted, the majority element (which appears more than half the time) will always be at this index, or very close to it, because it must occupy more than half of the list. Thus, this element will be the correct majority element.
        # return the mid element since it will always dominant if sorted
        nums.sort()
        return nums[len(nums)//2]
