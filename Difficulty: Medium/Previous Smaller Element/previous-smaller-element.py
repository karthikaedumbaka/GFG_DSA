class Solution:
	def prevSmaller(self, arr):
		# code here
		n = len (arr)
		result = [-1] * n
		stk = []
		for i in range(n):
		    while stk and arr[stk[-1]] >= arr[i]:
		        stk.pop()
		        
            if stk:
                result[i] = arr[stk[-1]]

		        
		    
		    
		    stk.append(i)
		    
        return result