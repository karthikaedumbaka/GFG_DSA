class Solution:
    def nextLargerElement(self, arr):
        # code here
        # filnd next greatest element 
        # Brute Force
        # n = len(arr)
        # ans=[-1]*n
        # for i in range(len(arr)):  #6   # fisrt pointer 
        #     for j in range(i+1,len(arr)):#8 # secound pointer for chack the greater number
        #         if arr[j] > arr[i]: # checking the condition
        #             ans[i] = ans[j]
        #             break # once we file the next greater element break the loop
        
        # return ans
        
        
        # 
        result = [-1]* len(arr)
        
        stk = [ ]
        
        for i in range(len(arr)-1,-1,-1):
            while stk and arr[i] >= stk[-1]:
                stk.pop()
                
            if stk:
                result[i] = stk[-1]
                
            
            stk.append(arr[i])
        
        return result
        
        