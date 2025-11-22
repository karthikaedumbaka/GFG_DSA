class Solution:
    def largest(self, arr):
        # code here
        i = arr[0]
        for j in range(1,len(arr)):
            if i < arr[j]:
                i = arr[j]
        return i 
        
