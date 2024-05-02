# Created by asetti2002 at 2024/04/25 19:25
# leetgo: 1.4.3
# https://leetcode.com/problems/consecutive-numbers-sum/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        count = 1
        for k in range(2, int((2 * n) ** 0.5) + 1):
            if (n - (k * (k - 1)) // 2) % k == 0:
                count += 1
        return count
# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().consecutiveNumbersSum(n)
    print("\noutput:", serialize(ans, "integer"))
