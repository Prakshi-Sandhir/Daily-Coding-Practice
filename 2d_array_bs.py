# https://leetcode.com/problems/search-a-2d-matrix/
class Solution(object):
    def searchMatrix(self, matrix, target):
        rows = len(matrix)
        cols = len(matrix[0])
        st,lst=0,cols-1
        st_row,lst_row=0,rows-1
        while st_row<=lst_row:
            mid_row=(st_row+lst_row)//2
            if target>matrix[mid_row][lst]:
                st_row=mid_row+1
            elif target<matrix[mid_row][st]:
                lst_row=mid_row-1
            elif target>=matrix[mid_row][st] and target<=matrix[mid_row][lst]:
                mid=(st+lst)//2
                if matrix[mid_row][mid]==target:
                    return True
                    break
                elif target>matrix[mid_row][mid]:
                    st=mid+1
                else:
                    lst=mid-1
        return False