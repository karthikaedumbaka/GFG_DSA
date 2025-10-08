from collections import Counter
class Solution:
    def frequencyCount(self, arr):
        #  code here
        result =[0]*len(arr)
        arrCount=Counter(arr)
        for index, value in arrCount.items():
            result[index-1]=value
        return result

