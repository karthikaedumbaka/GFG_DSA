class Solution:
    def findFloor(self, arr, x):
        l, r = 0, len(arr) - 1
        floor = -1

        while l <= r:
            mid = (l + r) // 2
            if arr[mid] == x:
                floor = mid     # record this as possible floor
                l = mid + 1     # move right to find last occurrence
            elif arr[mid] < x:
                floor = mid
                l = mid + 1
            else:
                r = mid - 1

        return floor
