class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for num in nums:
            result ^= num
        return result

# XOR is a math/computer operation that compares two numbers bit by bit.
# Think of it like “comparing bits”: if two bits are the same, XOR gives 0. If two bits are different, XOR gives 1.
# Example in binary:
# 5 = 0101
# 3 = 0011
# ------------
# 5 XOR 3 = 0110 (which is 6 in decimal)
        