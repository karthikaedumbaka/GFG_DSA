#User function Template for python3

class Solution:
    def evenlyDivides(self, n):
        # code here
        original = n
        count = 0
        
        while n > 0:
            digit = n % 10      # extract last digit
            if digit != 0 and original % digit == 0:
                count += 1
            n //= 10            # remove last digit
        
        return count