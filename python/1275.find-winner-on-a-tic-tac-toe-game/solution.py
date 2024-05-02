# Created by asetti2002 at 2024/04/25 20:25
# leetgo: 1.4.3
# https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        def check_winner(board):
            for i in range(3):
                if board[i][0] == board[i][1] == board[i][2] != " ":
                    return board[i][0]
                if board[0][i] == board[1][i] == board[2][i] != " ":
                    return board[0][i]
            if board[0][0] == board[1][1] == board[2][2] != " ":
                return board[0][0]
            if board[0][2] == board[1][1] == board[2][0] != " ":
                return board[0][2]
            return None
        
        board = [[" " for _ in range(3)] for _ in range(3)]
        player = "A"
        
        for i, (row, col) in enumerate(moves):
            board[row][col] = player
            player = "B" if i % 2 == 0 else "A"
        
        winner = check_winner(board)
        
        if winner:
            return winner
        elif len(moves) == 9:
            return "Draw"
        else:
            return "Pending"
# @lc code=end

if __name__ == "__main__":
    moves: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().tictactoe(moves)
    print("\noutput:", serialize(ans, "string"))
