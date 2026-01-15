class Solution:
    def nextLargerElement(self, arr):
        # code here
        n = len(arr)
        result = [-1] * n
        stk = []
        for i in range(n):
            while stk and arr[stk[-1]] < arr [i] :
                idx = stk.pop()
                result [ idx] = arr[i]
            stk.append(i)
            
        return result
        
        '''
        n=5
        
        i = 0 , stk=[] , result = [-1,-1,-1,-1,-1] ; condition will fail => stk[0]
        i = 1 , stk [0] , result = [-1,-1,-1,-1,-1] ; stk and arr[0] < arr[1] , 1<3
            condition is true 
            idx = 0
            result[0] = arr[1]  => result = [3,-1,-1,-1,] >stk = [1]
        i =2 ,stk [1] , result = [3,-1,-1,-1,-1] ; stk  and arr[1] < arr[2] , 3<2
            condition is false
             result = [3,-1,-1,-1,] >stk = [1,2]
        i=3 , stk= [1,2] ,  result = [3,-1,-1,-1,-1] , stk and arr[2] < arr[3] ,2<4
            condition is true
            result = [3,-1,4,-1] , stk = [1]
            stk and arr[1] < arr[3] ,3<4
            result = [3,4,4,-1] , stk = [0]
            
        i =4 ,stk =[] ,result = [3,4,4,-1] , stk= [4]
        
        return result = [3,4,4,-1]
        
        '''