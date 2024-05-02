# Created by asetti2002 at 2024/05/01 20:20
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-difference-by-remapping-a-digit/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def minMaxDifference(self, num: int) -> int:
        return int(''.join(sorted(str(num)).replace('0', '9', 1))) - int(''.join(sorted(str(num)).replace('1', '0', 1)))
# @lc code=end

if __name__ == "__main__":
    num: int = deserialize("int", read_line())
    ans = Solution().minMaxDifference(num)
    print("\noutput:", serialize(ans, "integer"))
