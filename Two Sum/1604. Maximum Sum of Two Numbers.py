## hash
## O(n), n is length of A
## Microsoft

class Solution:
    """
    @param A: An Integer array
    @return: returns the maximum sum of two numbers
    """
    def digit_sum(self, n):
        result = 0
        while n >= 10:
            result += n % 10
            n = n // 10
        result += n
        return result
        
    def MaximumSum(self, A):
        # write your code here
        result, dict = -1, {}
        for x in A:
            temp = self.digit_sum(x)
            if temp not in dict:
                dict[temp] = [x]
            else:
                dict[temp].append(x)
        
        for key, value in dict.items():
            if len(value) < 2:
                continue
            value = sorted(value)
            n = len(value)
            result = max(result, value[n-1] + value[n-2])
        return result
