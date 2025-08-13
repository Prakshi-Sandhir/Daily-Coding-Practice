#User function Template for python3
# https://www.geeksforgeeks.org/problems/ceil-the-floor2802/1
class Solution:
    def getFloorAndCeil(self, x: int, arr: list) -> list:
        arr.sort()
        n = len(arr)
        floor_val, ceil_val = -1, -1
        low, high = 0, n - 1
    
        while low <= high:
            mid = (low + high) // 2
    
            if arr[mid] == x:
                return [arr[mid], arr[mid]]  
            elif arr[mid] < x:
                floor_val = arr[mid]        
                low = mid + 1
            else:
                ceil_val = arr[mid]        
                high = mid - 1
    
        return [floor_val, ceil_val]       
        