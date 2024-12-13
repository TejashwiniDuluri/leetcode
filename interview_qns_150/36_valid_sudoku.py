from typing import List
from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set) 
        #=> total 9 squares and they will be identified by 
        #row => 0,1,2
        #col => 0,1,2
        # when you do //3 it will represent the square. Suppose you are at 0/0 grid its is 0th square i.e 0//3 => and 0//3 => 0
        # simalar whay if you are in second square 3//3 => 1 so its 1 square grid.


        # first square will have 9 elemnts as they fall in first square. How to represent first square is // by sqaue side i. eif your square size is 3, then 0/0 => grid can be identified as first sqaure like 0//3 =>0 and 0//3 =0 so it falls in 0th square.
        # this way we will index square grids as rows => 0, 1, 2 and columns => 0,1,2 so total there will be 9 square grids.
        # Identify your key to track sqauare as row//3 and col//3 because every row and col //3 will give 0 only for first square.

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".": # no element so skip.
                    continue
                if (board[row][col] in rows[row]) or (board[row][col] in cols[col]) or (board[row][col] in squares[f'{row//3}-{col//3}']):
                    return False
                else:
                    rows[row].add(board[row][col])
                    cols[col].add(board[row][col])
                    squares[f'{row//3}-{col//3}'].add(board[row][col])

        return True


obj = Solution()
board = board = [
 ["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
print(obj.isValidSudoku(board))