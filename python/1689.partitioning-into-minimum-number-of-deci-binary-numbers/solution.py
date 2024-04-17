# Created by asetti2002 at 2024/04/17 02:10
# leetgo: 1.4.3
# https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minPartitions(self, n: str) -> int:
        

# @lc code=end

if __name__ == "__main__":
    n: str = deserialize("str", read_line())
    ans = Solution().minPartitions(n)
    print("\noutput:", serialize(ans, "integer"))
