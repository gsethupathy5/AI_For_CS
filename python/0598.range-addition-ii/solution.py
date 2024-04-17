# Created by asetti2002 at 2024/04/17 02:16
# leetgo: 1.4.3
# https://leetcode.com/problems/range-addition-ii/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    m: int = deserialize("int", read_line())
    n: int = deserialize("int", read_line())
    ops: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().maxCount(m, n, ops)
    print("\noutput:", serialize(ans, "integer"))
