class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        answer = ""
        sortString = sorted(strs)

        first = sortString[0]
        last = sortString [-1]

        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return answer
            else:
                answer += first[i]
        return answer
        
# The notation first[i] is a common way across many programming languages to access an element at a specific index i in a collection, whether that collection is a string, list, array, or even some other data structure that supports indexing.




#         The reason why we sort the input array of strings and compare the first and last strings is that the longest common prefix of all the strings must be a prefix of the first string and a prefix of the last string in the sorted array. This is because strings are ordered based on their alphabetical order (Lexicographical order).
# For example, consider the input array of strings {"flower", "flow", "flight"}. After sorting the array, we get {"flight", "flow", "flower"}. The longest common prefix of all the strings is "fl", which is located at the beginning of the first string "flight" and the second string "flow". Therefore, by comparing the first and last strings of the sorted array, we can easily find the longest common prefix.