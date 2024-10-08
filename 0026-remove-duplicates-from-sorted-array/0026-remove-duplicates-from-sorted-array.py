class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # every time a new unique element is found, it will be placed at the current j index.
        # The reason j starts at 1 is that the first element (at index 0) is always considered unique,

        # While j is a value representing the number of unique elements, it is also used as an index during the process of modifying the array. The key point is that j is both a counter (tracking unique elements) and an index when placing those unique elements in the array.        because j start at 1, whenever a unique element is found, is will increment the position by 1, as well as the count value by 1, since j as a barrier, so position increment by 1 is the same as value increment by 1

        j = 1
        for i in range(1, len(nums)):
            # if nums[i] = nums[i-1], do nothing, if not, paste the element at j, which is the barrier of keeping track of unique elements
            if nums[i] != nums[i-1]:
                nums[j] = nums[i]
                j += 1
        return j



        