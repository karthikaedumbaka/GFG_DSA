class Solution:
    def leaders(self, arr):
        # code here
        n= len(arr)
        ans =[ ]
        i = arr[n-1]
        ans.append(arr[n-1])
        for j in range(n-2,-1,-1):
            if arr[j] >= i:
                ans.append(arr[j])
                i = arr[j]
        ans = ans[::-1]
        return ans
                
            
        