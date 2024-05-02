# Created by asetti2002 at 2024/04/25 20:06
# leetgo: 1.4.3
# https://leetcode.com/problems/alphabet-board-path/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        import string
        
        def get_pos(c):
            return (divmod(ord(c) - ord('a'), 5))
        
        def move(board, r1, c1, r2, c2):
            if r1 == r2 and c1 == c2:
                return ''
            elif r1 == 5 and c1 == c2:
                return 'U' + move(board, r1 - 1, c1, r2, c2)
            elif r1 == 4 and c1 == c2:
                return 'D' + move(board, r1 + 1, c1, r2, c2)
            elif c1 == 0 and r1 == r2:
                return 'R' + move(board, r1, c1 + 1, r2, c2)
            elif c1 == 4 and r1 == r2:
                return 'L' + move(board, r1, c1 - 1, r2, c2)
            elif c1 < c2:
                return 'R' + move(board, r1, c1 + 1, r2, c2)
            elif c1 > c2:
                return 'L' + move(board, r1, c1 - 1, r2, c2)
            elif r1 < r2:
                return 'D' + move(board, r1 + 1, c1, r2, c2)
            elif r1 > r2:
                return 'U' + move(board, r1 - 1, c1, r2, c2)
        
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        
        current_r, current_c = 0, 0
        result = ''
        
        for char in target:
            tr, tc = get_pos(char)
            result += move(board, current_r, current_c, tr, tc) + '!'
            current_r, current_c = tr, tc
        
        return result
# @lc code=end

if __name__ == "__main__":
    target: str = deserialize("str", read_line())
    ans = Solution().alphabetBoardPath(target)
    print("\noutput:", serialize(ans, "string"))
