# Created by asetti2002 at 2024/04/17 02:07
# leetgo: 1.4.3
# https://leetcode.com/problems/minimized-maximum-of-products-distributed-to-any-store/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    quantities: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minimizedMaximum(n, quantities)
    print("\noutput:", serialize(ans, "integer"))
