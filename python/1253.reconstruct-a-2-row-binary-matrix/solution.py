# Created by asetti2002 at 2024/04/17 02:12
# leetgo: 1.4.3
# https://leetcode.com/problems/reconstruct-a-2-row-binary-matrix/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        

# @lc code=end

if __name__ == "__main__":
    upper: int = deserialize("int", read_line())
    lower: int = deserialize("int", read_line())
    colsum: List[int] = deserialize("List[int]", read_line())
    ans = Solution().reconstructMatrix(upper, lower, colsum)
    print("\noutput:", serialize(ans, "integer[][]"))
