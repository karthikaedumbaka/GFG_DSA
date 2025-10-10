#User function Template for python3

class Solution:
    def printGfg(self, n):
        # Code here
        string ="GFG"
        if n==0:
            return
        self.printGfg(n-1)
        print(string,end=' ')