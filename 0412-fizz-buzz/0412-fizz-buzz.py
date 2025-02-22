class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        answers =[]
        for i in range(1,n+1):
            if (i % 3 == 0) and (i % 5 == 0):
                answers.append('FizzBuzz')
            elif i % 5 == 0:
                answers.append('Buzz')
            elif i % 3 == 0:
                answers.append('Fizz')
            else:
                answers.append(str(i))
        return answers
            
        