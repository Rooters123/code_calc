# encoding = utf-8
class Solution:
    def isValidSudoku(self, board):
        def calcfun(data):
            list_data = list(filter(lambda x:x != ".",data))
            return len(set(list_data)) != len(list_data)
        for row in board:
            if calcfun(row):
                return False
        for column in zip(*board):
            if calcfun(column):
                return False

        for row in range(3):
            for column in range(3):
                area = [board[i][j] for i in range(row * 3,row * 3 + 3) for j in range(column * 3,column * 3 + 3)]
                if calcfun(area):
                    return False
        return True
    def isValidSudoku2(self,board):
        # （1）行列去重的长度和之前的行列长度是否一致
        # （2）类似于CA模拟，开窗为3*3矩阵进行判断，这里的前提是能够被3整除
        def calcfun(data):
            new_list = list(filter(lambda x: x != ".",data))
            return len(set(new_list)) == len(data)
        for row in board:
            if not calcfun(row):
                return False
        for col in zip(*board):
            if not calcfun(col):
                return False
        for i in range(3):
            for j in range(3):
                area_list = [board[i][j] for i in range(i*3,i*3+3) for j in range(j*3,j*3+3)]
                if not  area_list:
                    return False
        return True
data = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
s =Solution()
# print(s.isValidSudoku2(data))

print(list(zip(*data)))

# for column in zip(*data):  # 9列
#     print(column)




