class Solution:
	def nextSmallerEle(self, arr):
		# code here
		
		n = len(arr)
		result = [-1] * n
		stk = []
		
		for i in range(n) :
		    while stk and arr[stk[-1]] > arr[i]: 
		        idx = stk.pop()
		        result[idx] = arr[i]
            
            stk.append(i)
            
        return result