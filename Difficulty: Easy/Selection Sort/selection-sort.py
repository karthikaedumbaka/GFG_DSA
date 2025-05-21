#User function Template for python3

class Solution: 
    def selectionSort(self, arr):
        #code here
        n=len(arr)
        for i in range(0,n):
            mid=i
            for j in range(i+1,n):
                if arr[mid]>arr[j]:
                    mid=j
            arr[mid],arr[i]=arr[i],arr[mid]
        return arr
            


#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        arr = [int(i) for i in input().split()]

        obj = Solution()
        obj.selectionSort(arr)

        IntArray().Print(arr)
        print("~")

# } Driver Code Ends