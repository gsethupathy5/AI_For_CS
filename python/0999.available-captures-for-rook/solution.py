# Created by asetti2002 at 2024/04/25 19:51
# leetgo: 1.4.3
# https://leetcode.com/problems/available-captures-for-rook/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        def find_rook(board):
            for i in range(8):
                for j in range(8):
                    if board[i][j] == 'R':
                        return (i, j)
        
        def find_attackables(board, i, j):
            count = 0
            for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_i, new_j = i, j
                while 0 <= new_i < 8 and 0 <= new_j < 8:
                    if board[new_i][new_j] == 'B':
                        break
                    if board[new_i][new_j] == 'p':
                        count += 1
                        break
                    new_i += x
                    new_j += y
            return count
        
        rook_i, rook_j = find_rook(board)
        return find_attackables(board, rook_i, rook_j)
# @lc code=end

if __name__ == "__main__":
    board: List[List[str]] = deserialize("List[List[str]]", read_line())
    ans = Solution().numRookCaptures(board)
    print("\noutput:", serialize(ans, "integer"))
