#User function Template for python3
from math import sqrt
class Solution:
    def isPrime(self, n):
        # code here
        
        if n==1:
            return False 
        count=[]
        for i in range(1,int(sqrt(n)+1)):
            if n%i==0:
                count.append(i)
                if n//i !=i:
                    count.append(n//i )
        if len(count)>2:
            return False
        return True
                
            
                


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())  # Read number of test cases
    for _ in range(t):
        n = int(input())  # Read the number to check primality

        ob = Solution()
        # Using Python's conditional expression for true/false
        print("true" if ob.isPrime(n) else
              "false")  # Print "true" if prime, else "false"
        print("~")

# } Driver Code Ends