# Created by asetti2002 at 2024/04/17 02:16
# leetgo: 1.4.3
# https://leetcode.com/problems/largest-plus-sign/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    mines: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().orderOfLargestPlusSign(n, mines)
    print("\noutput:", serialize(ans, "integer"))
