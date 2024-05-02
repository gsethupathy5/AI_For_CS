# Created by asetti2002 at 2024/05/01 20:01
# leetgo: 1.4.3
# https://leetcode.com/problems/sum-of-number-and-its-reverse/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        return num % 10 != 0 or num == 0
# @lc code=end

if __name__ == "__main__":
    num: int = deserialize("int", read_line())
    ans = Solution().sumOfNumberAndReverse(num)
    print("\noutput:", serialize(ans, "boolean"))
