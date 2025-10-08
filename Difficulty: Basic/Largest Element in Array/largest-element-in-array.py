class Solution:
    def largest(self, arr):
        # code here
        max_value=float("-inf")
        for i in arr:
            max_value = max(max_value,i)
        return max_value
        
