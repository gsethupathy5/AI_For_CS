# Created by asetti2002 at 2024/05/01 20:05
# leetgo: 1.4.3
# https://leetcode.com/problems/find-the-pivot-integer/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def pivotInteger(self, n: int) -> int:
        total_sum = n * (n + 1) // 2
        if total_sum % 2 == 0:
            target_sum = total_sum // 2
            current_sum = 0
            for i in range(1, n + 1):
                current_sum += i
                if current_sum == target_sum:
                    return i
                elif current_sum > target_sum:
                    return -1
        else:
            return -1
# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().pivotInteger(n)
    print("\noutput:", serialize(ans, "integer"))
