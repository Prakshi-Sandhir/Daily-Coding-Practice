# https://www.geeksforgeeks.org/problems/reverse-an-array/1
class Solution:
    def reverseArray(self, arr):
        n=len(arr)
        temp,count=0,0
        st,lst=0,n-1
        while st<lst:
            arr[st],arr[lst] = arr[lst],arr[st]
            st+=1
            lst-=1
        return arr
            
            
        
        
        
        
        
        


