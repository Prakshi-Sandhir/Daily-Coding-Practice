# https://leetcode.com/problems/search-a-2d-matrix-ii/
class Solution(object):
    def searchMatrix(self, matrix, target):
        rows = len(matrix)
        cols = len(matrix[0])
        st,lst=0,cols-1
        st_row,lst_row=0,rows-1
        while st<rows and lst>=0:
                if matrix[st][lst]==target:
                    return True
                    break
                elif target<matrix[st][lst]:
                    lst-=1
                else:
                    st+=1
        return False