# https://www.geeksforgeeks.org/problems/number-of-occurrence2259/1
class Solution:
    def countFreq(self, arr, target):
        tem = len(arr)
        st, lst = 0, tem - 1
        first = -1
        
        while st <= lst:
            mid = (st + lst) // 2
            if arr[mid] == target:
                first = mid
                lst = mid - 1
            elif arr[mid] < target:
                st = mid + 1
            else:
                lst = mid - 1
                
        if first == -1:
            return 0
        st, lst = 0, tem - 1
        last = -1
        while st <= lst:
            mid = (st + lst) // 2
            if arr[mid] == target:
                last = mid
                st = mid + 1
            elif arr[mid] < target:
                st = mid + 1
            else:
                lst = mid - 1
        
        return last - first + 1
