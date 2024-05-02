# Created by asetti2002 at 2024/05/01 20:02
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-addition-to-make-integer-beautiful/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        x = max(0, (target - sum(int(i) for i in str(n)) + 9) // 10 * 10)
        return x
# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().makeIntegerBeautiful(n, target)
    print("\noutput:", serialize(ans, "long"))
