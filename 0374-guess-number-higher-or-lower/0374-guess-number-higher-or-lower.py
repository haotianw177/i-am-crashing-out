# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 0
        r = n

        while l <= r:
            mid = (l + r) // 2  # Dynamically calculate midpoint
            result = guess(mid)  # Get feedback for the guess
            
            if result < 0:  # If guessed number is too high
                r = mid - 1  # Narrow the range to [l, mid - 1]
            elif result > 0:  # If guessed number is too low
                l = mid + 1  # Narrow the range to [mid + 1, r]
            else:  # If guessed number is correct
                return mid


            # so l = 1, is value 1, and n is upperbound limit of a number value


        
        