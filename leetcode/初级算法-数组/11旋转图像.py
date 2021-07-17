# encoding = utf-8
class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix[:] = [list(row)[::-1] for row in zip(*matrix)]
        print(matrix)
s =Solution()
s.rotate([[1,2,3],[4,5,6],[7,8,9]])

