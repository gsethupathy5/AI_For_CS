# Created by asetti2002 at 2024/04/25 20:30
# leetgo: 1.4.3
# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        while num != 0:
            if num % 2 == 0:
                num /= 2
            else:
                num -= 1
            steps += 1
        return steps
# @lc code=end

if __name__ == "__main__":
    num: int = deserialize("int", read_line())
    ans = Solution().numberOfSteps(num)
    print("\noutput:", serialize(ans, "integer"))
