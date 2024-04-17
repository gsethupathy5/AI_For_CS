# Created by asetti2002 at 2024/04/17 02:13
# leetgo: 1.4.3
# https://leetcode.com/problems/sequential-digits/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    low: int = deserialize("int", read_line())
    high: int = deserialize("int", read_line())
    ans = Solution().sequentialDigits(low, high)
    print("\noutput:", serialize(ans, "integer[]"))
