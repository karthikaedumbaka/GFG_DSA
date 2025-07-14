from collections import deque
class Solution:
    def nextLargerElement(self, arr):
        # code here
        result=[-1]*len(arr)
        stk = []
        for i in range(len(arr) - 1, -1, -1):
            # Remove all smaller or equal elements from the stack
            while stk and stk[-1] <= arr[i]:
                stk.pop()

            # If stack is not empty, the top is the next greater element
            if stk:
                result[i] = stk[-1]

            # Push the current element to stack
            stk.append(arr[i])

        return result
