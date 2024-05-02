# Created by asetti2002 at 2024/05/01 20:15
# leetgo: 1.4.3
# https://leetcode.com/problems/split-with-minimum-sum/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def splitNum(self, num: int) -> int:
        pass
# @lc code=end

if __name__ == "__main__":
    num: int = deserialize("int", read_line())
    ans = Solution().splitNum(num)
    print("\noutput:", serialize(ans, "integer"))
