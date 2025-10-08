"""
You're given an array (arr)
Return the frequency of element x in the given array
"""
from collections import Counter
class Solution:
    def findFrequency(self, arr, x):
        # code here
        frequencyCount = Counter(arr)
        return frequencyCount[x]