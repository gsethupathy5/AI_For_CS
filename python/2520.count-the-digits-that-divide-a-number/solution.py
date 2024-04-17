# Created by asetti2002 at 2024/04/17 02:04
# leetgo: 1.4.3
# https://leetcode.com/problems/count-the-digits-that-divide-a-number/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def countDigits(self, num: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    num: int = deserialize("int", read_line())
    ans = Solution().countDigits(num)
    print("\noutput:", serialize(ans, "integer"))
