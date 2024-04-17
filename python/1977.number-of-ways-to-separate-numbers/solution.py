# Created by asetti2002 at 2024/04/17 02:08
# leetgo: 1.4.3
# https://leetcode.com/problems/number-of-ways-to-separate-numbers/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def numberOfCombinations(self, num: str) -> int:
        

# @lc code=end

if __name__ == "__main__":
    num: str = deserialize("str", read_line())
    ans = Solution().numberOfCombinations(num)
    print("\noutput:", serialize(ans, "integer"))
